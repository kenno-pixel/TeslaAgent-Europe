import sqlite3
from pathlib import Path


DATABASE_FILE = Path(__file__).parent.parent / "teslaagent.db"


def initialize_database() -> None:
    """Create the SQLite database and tables if they do not exist."""

    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT NOT NULL,
            listing_id TEXT NOT NULL,
            url TEXT NOT NULL,
            model TEXT NOT NULL,
            version TEXT NOT NULL,
            price INTEGER NOT NULL,
            mileage INTEGER NOT NULL,
            registration TEXT,
            country TEXT,
            score INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    initialize_database()
    print("Database created successfully.")