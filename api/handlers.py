from api.codes import normalize_code
from cache.link_cache import LinkCache
from storage.db import get_link

cache = LinkCache(max_size=10_000)


def redirect(code: str):
    code = normalize_code(code)
    url = cache.get(code) or get_link(code)
    if url is None:
        return 404, None
    cache.set(code, url)
    return 302, url
