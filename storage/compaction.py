import logging

from storage.db import connect

log = logging.getLogger(__name__)

BATCH_SIZE = 1_000


def compact_clicks() -> None:
    """Roll raw click rows up into daily totals, one transaction per batch."""
    conn = connect()
    try:
        while True:
            with conn:
                ids = [r[0] for r in conn.execute("SELECT id FROM raw_clicks LIMIT ?", (BATCH_SIZE,))]
                if not ids:
                    log.info("compaction finished")
                    break
                marks = ",".join("?" * len(ids))
                conn.execute(
                    f"INSERT INTO daily_clicks SELECT code, day, COUNT(*) FROM raw_clicks WHERE id IN ({marks}) "
                    "GROUP BY code, day ON CONFLICT (code, day) DO UPDATE SET clicks = clicks + excluded.clicks",
                    ids,
                )
                conn.execute(f"DELETE FROM raw_clicks WHERE id IN ({marks})", ids)
    finally:
        conn.close()
