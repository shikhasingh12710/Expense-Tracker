import sqlite3

def connect_db():
    return sqlite3.connect("expenses.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        category TEXT,
        amount REAL,
        date TEXT,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
