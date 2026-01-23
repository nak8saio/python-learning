import sqlite3
import os

DB_PATH = os.path.join("data","employees.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = get_connection()
    cusor = conn.cursor()

    cusor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  monthly_salary INTEGER,
                  annual_salary INTEGER,
                  category TEXT
                  )
                  """)
    conn.commit()
    conn.close()
