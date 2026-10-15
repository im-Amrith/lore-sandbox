import redis

TTL_SECONDS = 24 * 60 * 60


class LinkCache:
    """Shared Redis cache of short code -> target URL, 24h TTL."""

    def __init__(self, url: str = "redis://cache:6379/0"):
        self._redis = redis.Redis.from_url(url, decode_responses=True)

    def get(self, code: str):
        return self._redis.get(f"link:{code}")

    def set(self, code: str, url: str) -> None:
        self._redis.set(f"link:{code}", url, ex=TTL_SECONDS)

    def delete(self, code: str) -> None:
        self._redis.delete(f"link:{code}")
