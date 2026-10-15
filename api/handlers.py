from cache.link_cache import WARM_TOP_N, LinkCache
from messaging import pubsub
from storage.db import get_link, top_links

cache = LinkCache(pubsub)


def on_startup():
    # Avoid cold starts after a deploy: warm the hottest links on boot.
    cache.warm(top_links(WARM_TOP_N))


def redirect(code: str):
    # Codes are case-sensitive: never change their case before lookup.
    code = code.strip()
    url = cache.get(code) or get_link(code)
    if url is None:
        return 404, None
    cache.set(code, url)
    return 302, url


def edit_link(code: str, new_url: str):
    # Publishes an invalidation that every replica applies.
    cache.invalidate(code)
    return 200, new_url
