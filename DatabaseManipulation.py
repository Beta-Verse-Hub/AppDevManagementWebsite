import sqlite3

conn = sqlite3.connect('Database.db')
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('projects',))

if not c.fetchone():
    c.execute("""
            CREATE TABLE projects (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                programmers TEXT NOT NULL,
                link TEXT NOT NULL
            )
    """)

conn.commit()
conn.close()