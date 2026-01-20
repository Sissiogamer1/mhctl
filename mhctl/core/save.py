import sqlite3
from pathlib import *
from datetime import *

db_path = Path(__file__).parent.parent / "data" / "uploads.db"

def save_uguu(original_filename: str, url: str, provider: str, size: str):
    print(f"TENTATIVO CON {db_path}")
    conn = sqlite3.connect(db_path)
    print(f"original_filename: {original_filename}\nurl: {url}\nprovider: {provider}\nsize: {size}")
    try:
        conn.execute(
        "INSERT INTO uploads (original_filename, url, provider, timestamp, size) VALUES (?, ?, ?, ?, ?)",
        (original_filename, url, provider, datetime.now().isoformat(), size)
        )
    except sqlite3.IntegrityError:
        # L'URL esiste già (violazione del constraint UNIQUE)
        raise ValueError(f"URL already exists in database: {url}")
    finally:
        conn.commit()
        print("MESSO NEL DATABASE")
        conn.close()