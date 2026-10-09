import sqlite3

DB_PATH = "tern.db"
TIMEOUT_SECONDS = 5


def connect():
    return sqlite3.connect(DB_PATH, timeout=TIMEOUT_SECONDS)


def get_link(code: str):
    with connect() as conn:
        row = conn.execute("SELECT url FROM links WHERE code = ?", (code,)).fetchone()
    return row[0] if row else None
