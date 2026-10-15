from api.codes import normalize_code
from cache.link_cache import LinkCache
from storage.db import get_link

cache = LinkCache()


def redirect(code: str):
    code = normalize_code(code)
    url = cache.get(code) or get_link(code)
    if url is None:
        return 404, None
    cache.set(code, url)
    return 302, url


def edit_link(code: str, new_url: str):
    # One delete invalidates the link for every replica.
    cache.delete(code)
    return 200, new_url
