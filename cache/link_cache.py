from collections import OrderedDict


class LinkCache:
    """Per-process LRU of short code -> target URL."""

    def __init__(self, max_size: int = 10_000):
        self.max_size = max_size
        self._items: OrderedDict[str, str] = OrderedDict()

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

    def delete(self, code: str) -> None:
        self._items.pop(code, None)
