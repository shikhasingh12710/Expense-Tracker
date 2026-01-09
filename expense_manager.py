from database import connect_db

def add_expense(txn_type, category, amount, date, description):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses (type, category, amount, date, description)
    VALUES (?, ?, ?, ?, ?)
    """, (txn_type, category, amount, date, description))

    conn.commit()
    conn.close()

def get_all_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()

    conn.close()
    return data
