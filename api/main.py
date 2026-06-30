from fastapi import FastAPI
from sqlalchemy import text
from api.database import engine

app = FastAPI(
    title="Medical Telegram Warehouse API",
    version="1.0"
)

# -------------------------------------------------------
# Top Products
# -------------------------------------------------------
@app.get("/api/reports/top-products")
def top_products():

    query = """
    SELECT
        message_text AS product_name,
        COUNT(*) AS mention_count
    FROM telegram_messages
    GROUP BY message_text
    ORDER BY mention_count DESC
    LIMIT 10;
    """

    with engine.connect() as conn:
        result = conn.execute(text(query))

        return [
            dict(row._mapping)
            for row in result
        ]


# -------------------------------------------------------
# Channel Activity
# -------------------------------------------------------
@app.get("/api/channels/{channel_name}/activity")
def channel_activity(channel_name: str):

    query = """
    SELECT
        channel_name,
        COUNT(*) AS total_messages
    FROM telegram_messages
    WHERE channel_name = :channel
    GROUP BY channel_name;
    """

    with engine.connect() as conn:
        result = conn.execute(
            text(query),
            {"channel": channel_name}
        )

        return [
            dict(row._mapping)
            for row in result
        ]


# -------------------------------------------------------
# Search Messages
# -------------------------------------------------------
@app.get("/api/search/messages")
def search_messages(keyword: str):

    query = """
    SELECT
        message_id,
        message_text
    FROM telegram_messages
    WHERE message_text ILIKE :search;
    """

    with engine.connect() as conn:
        result = conn.execute(
            text(query),
            {"search": f"%{keyword}%"}
        )

        return [
            dict(row._mapping)
            for row in result
        ]


# -------------------------------------------------------
# Visual Content Report
# -------------------------------------------------------
@app.get("/api/reports/visual-content")
def visual_content():

    query = """
    SELECT
        detected_class,
        COUNT(*) AS total
    FROM image_detections
    GROUP BY detected_class
    ORDER BY total DESC;
    """

    with engine.connect() as conn:
        result = conn.execute(text(query))

        return [
            dict(row._mapping)
            for row in result
        ]
