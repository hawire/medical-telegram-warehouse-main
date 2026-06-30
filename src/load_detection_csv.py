import pandas as pd
import psycopg2

df = pd.read_csv("data/processed/detections.csv")

conn = psycopg2.connect(
    host="localhost",
    database="medical",
    user="postgres",
    password="password"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS raw.image_detections(

message_id TEXT,

channel_name TEXT,

detected_class TEXT,

confidence_score FLOAT,

image_category TEXT

)
""")

for _, row in df.iterrows():

    cur.execute("""
    INSERT INTO raw.image_detections
    VALUES(%s,%s,%s,%s,%s)
    """, (
        row.message_id,
        row.channel_name,
        row.detected_class,
        row.confidence_score,
        row.image_category
    ))

conn.commit()

cur.close()

conn.close()

print("Detection data loaded successfully.")
