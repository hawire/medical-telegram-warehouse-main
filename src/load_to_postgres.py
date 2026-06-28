
import json
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="medical",
    user="postgres",
    password="password"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS telegram_messages(
    message_id INTEGER,
    message_text TEXT,
    views INTEGER,
    forwards INTEGER
)
""")

conn.commit()

cur.close()
conn.close()
