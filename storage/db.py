import sqlite3

DB_PATH = "tern.db"


def connect():
    return sqlite3.connect(DB_PATH)


def get_link(code: str):
    with connect() as conn:
        row = conn.execute("SELECT url FROM links WHERE code = ?", (code,)).fetchone()
    return row[0] if row else None
