import sqlite3

conn = sqlite3.connect("tasks.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT DEFAULT 'Pending'
)
""")

conn.commit()
conn.close()

print("tasks.db created successfully")
