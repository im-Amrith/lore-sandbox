from collections import Counter
from datetime import date

_counts: Counter = Counter()

# Clicks are recorded by the redirect handler only. The cache layer used to
# emit its own event on every hit, which double-counted cached redirects.
COUNTED_SOURCES = {"handler"}


def record_click(code: str, day: date | None = None, source: str = "handler") -> None:
    if source not in COUNTED_SOURCES:
        return
    _counts[(code, day or date.today())] += 1


def clicks_for(code: str, day: date) -> int:
    return _counts[(code, day)]


def reset() -> None:
    """Clear all counts (used by tests and the backfill script)."""
    _counts.clear()
