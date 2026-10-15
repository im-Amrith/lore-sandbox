import secrets
import string

ALPHABET = string.ascii_letters + string.digits  # base62
CODE_LENGTH = 7  # 62**7 ~= 3.5 trillion codes
MAX_ATTEMPTS = 5


def random_code() -> str:
    return "".join(secrets.choice(ALPHABET) for _ in range(CODE_LENGTH))


def new_code(exists) -> str:
    """Return a random code that `exists(code)` says is unused, retrying on collision."""
    for _ in range(MAX_ATTEMPTS):
        code = random_code()
        if not exists(code):
            return code
    raise RuntimeError("could not find a free short code")


def normalize_code(code: str) -> str:
    return code.strip().lower()
