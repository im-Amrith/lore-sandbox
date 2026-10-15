import csv
import io

from analytics.clicks import _counts


def export_csv() -> str:
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["code", "day", "clicks"])
    for (code, day), n in sorted(_counts.items()):
        writer.writerow([code, day.isoformat(), n])
    return buf.getvalue()
