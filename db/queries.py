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
        ('Баянета', 30, 'https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fkingame.ru%2Fwp-content%2Fuploads%2Ff%2Fb%2F8%2Ffb8800b7d1f95df0777189b57937fc3d.jpeg&lr=10309&pos=1&rpt=simage&text=%D0%B1%D0%B0%D0%B9%D0%BE%D0%BD%D0%B5%D1%82%D1%82%D0%B0%20%D1%84%D0%B8%D0%B3%D1%83%D1%80%D0%BA%D0%B8'),
        ('2B', 15, 'https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fae01.alicdn.com%2Fkf%2FH4a61cc573c3b4259abeadc007010197d6%2FNieR-Automata-YoRHa-No-2-Type-B-2B-PVC-Figure-Collectible-Model-Toy.jpg&lr=10309&pos=0&rpt=simage&text=2B%20%D1%84%D0%B8%D0%B3%D1%83%D1%80%D0%BA%D0%B8'),
        ('Альбедо', 40, 'https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fwoody-comics.ru%2Fimages%2Fthumbnails%2F1959%2F1444%2Fdetailed%2F96%2F38bad4190045521e2e676669afe61921.jpg&lr=10309&pos=12&rpt=simage&text=%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE%20%D1%84%D0%B8%D0%B3%D1%83%D1%80%D0%BA%D0%B8')
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