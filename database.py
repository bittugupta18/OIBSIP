import sqlite3


def create_table():
    conn = sqlite3.connect("bmi_history.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bmi_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight REAL NOT NULL,
            height REAL NOT NULL,
            bmi REAL NOT NULL,
            category TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_record(name, weight, height, bmi, category):
    conn = sqlite3.connect("bmi_history.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bmi_records
        (name, weight, height, bmi, category)
        VALUES (?, ?, ?, ?, ?)
    """, (name, weight, height, bmi, category))

    conn.commit()
    conn.close()


create_table()
def get_records():
    conn = sqlite3.connect("bmi_history.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, weight, height, bmi, category
        FROM bmi_records
    """)

    records = cursor.fetchall()

    conn.close()
    return records