import sqlite3

def init_db():
    conn = sqlite3.connect('app/database/ambulance.db')
    with open('app/database/schema.sql') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
