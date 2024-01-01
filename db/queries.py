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
        DROP TABLE IF EXISTS stationers
    """)
    cursor.execute("""
        DROP TABLE IF EXISTS figures
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS anime (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            episodes INTEGER,
            total_time TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stationers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            quantity INTEGER,
            stock TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS figures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            long INTEGER,
            image TEXT          
        )
    """)
    db.commit()


def populate_tables():
    cursor.execute("""
        INSERT INTO anime (title, episodes, total_time) VALUES
        ('Dragon Ball Super', 153, 'Около 3650 минут'),
        ('Атака титанов', 75, 'Около 1800 минут'),
        ('One Piece', 1000, 'Около 24 000 минут')
    """)
    cursor.execute("""
        INSERT INTO stationers (name, quantity, stock) VALUES
        ('Корандаши', 123, 'В наличии'),
        ('Брелки', 0, 'Скоро будет'),
        ('Ручки', 234, 'В наличии')
    """)
    cursor.execute("""
        INSERT INTO figures (name, long, image) VALUES 
        ('Баянета', 30, 'Byoneta.webp'),
        ('2B', 15, '2B.webp'),
        ('Альбедо', 40, 'Albedo.webp')
    """)
    db.commit()


conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

def get_anime():
    cursor.execute('SELECT * FROM anime')
    return cursor.fetchall()

def get_stationery():
    cursor.execute('SELECT * FROM stationers')
    return cursor.fetchall()

def get_figures():
    cursor.execute('SELECT * FROM figures')
    return cursor.fetchall()

if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()