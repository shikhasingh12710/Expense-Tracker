import sqlite3
import pandas as pd

def monthly_report():
    conn = sqlite3.connect("expenses.db")

    query = """
    SELECT strftime('%Y-%m', date) AS month,
           category,
           SUM(amount) AS total
    FROM expenses
    WHERE type='expense'
    GROUP BY month, category
    """

    df = pd.read_sql(query, conn)
    conn.close()

    return df

def detect_anomalies(threshold=2):
    conn = sqlite3.connect("expenses.db")
    df = pd.read_sql("SELECT * FROM expenses WHERE type='expense'", conn)
    conn.close()

    mean = df['amount'].mean()
    std = df['amount'].std()

    anomalies = df[df['amount'] > mean + threshold * std]
    return anomalies
