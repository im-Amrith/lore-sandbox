from collections import OrderedDict

INVALIDATION_CHANNEL = "link-invalidations"
WARM_TOP_N = 10_000


class LinkCache:
    """Per-replica LRU of short code -> target URL, kept in sync with pub/sub invalidation."""

    def __init__(self, pubsub, max_size: int = 100_000):
        self.max_size = max_size
        self._items: OrderedDict[str, str] = OrderedDict()
        self._pubsub = pubsub
        self._pubsub.subscribe(INVALIDATION_CHANNEL, self._on_invalidate)

    def get(self, code: str):
        if code in self._items:
            self._items.move_to_end(code)
            return self._items[code]
        return None

    def set(self, code: str, url: str) -> None:
        self._items[code] = url
        self._items.move_to_end(code)
        if len(self._items) > self.max_size:
            self._items.popitem(last=False)

    def invalidate(self, code: str) -> None:
        """Drop `code` here and tell every other replica to drop it too."""
        self._items.pop(code, None)
        self._pubsub.publish(INVALIDATION_CHANNEL, code)

    def _on_invalidate(self, code: str) -> None:
        self._items.pop(code, None)

    def warm(self, top_links) -> None:
        """Preload the most-clicked links so a fresh replica doesn't start cold."""
        for code, url in top_links[:WARM_TOP_N]:
            self.set(code, url)
