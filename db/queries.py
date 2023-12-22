import sqlite3
from pathlib import Path

def init_db():
    db_path = Path(__file__).parent.parent / "db.sqlite"
    global db, cursor
    db = sqlite3.connect(db_path)
    cursor = db.cursor()


def create_tables():
    cursor.execute("""
        DROP TABLE IF EXISTS anime
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS anime (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            episodes INTEGER,
            total_time TEXT
        )
    """)
    db.commit()

def populate_tables():
    cursor.execute("""
        INSERT INTO anime (title, episodes, total_time) VALUES
        ('Наруто', 220, 'Около 5000 минут'),
        ('Атака титанов', 75, 'Около 1800 минут'),
        ('Dragon Ball',  153 , ' Около 3650 минут')
    """)
    db.commit()


conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

def get_anime():
    cursor.execute('SELECT * FROM anime')
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    print(get_anime())