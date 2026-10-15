MAX_URL_LENGTH = 2048


def check_url(url: str) -> None:
    if len(url) > MAX_URL_LENGTH:
        raise ValueError("url too long")
    if not url.startswith(("http://", "https://")):
        raise ValueError("url must be http(s)")
