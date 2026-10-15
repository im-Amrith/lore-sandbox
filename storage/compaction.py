from storage.db import connect


def compact_clicks() -> None:
    """Roll raw click rows up into daily totals, in one transaction."""
    with connect() as conn:
        conn.execute(
            "INSERT INTO daily_clicks SELECT code, day, COUNT(*) FROM raw_clicks GROUP BY code, day"
        )
        conn.execute("DELETE FROM raw_clicks")
