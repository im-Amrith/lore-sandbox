from collections import Counter
from datetime import date

_counts: Counter = Counter()


def record_click(code: str, day: date | None = None) -> None:
    _counts[(code, day or date.today())] += 1


def clicks_for(code: str, day: date) -> int:
    return _counts[(code, day)]
