import string

ALPHABET = string.ascii_lowercase


def next_code(last: str) -> str:
    """Return the next sequential code after `last` (aaaa -> aaab)."""
    chars = list(last)
    i = len(chars) - 1
    while i >= 0:
        idx = ALPHABET.index(chars[i])
        if idx + 1 < len(ALPHABET):
            chars[i] = ALPHABET[idx + 1]
            return "".join(chars)
        chars[i] = ALPHABET[0]
        i -= 1
    return ALPHABET[0] + "".join(chars)


def normalize_code(code: str) -> str:
    return code.strip().lower()
