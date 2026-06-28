
from telethon import TelegramClient
import json
import os

API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"

client = TelegramClient("session", API_ID, API_HASH)

async def scrape(channel):
    messages = []

    async for msg in client.iter_messages(channel, limit=100):
        messages.append({
            "message_id": msg.id,
            "date": str(msg.date),
            "text": msg.text,
            "views": msg.views,
            "forwards": msg.forwards
        })

    os.makedirs(
        "data/raw/telegram_messages/2026-06-28",
        exist_ok=True
    )

    with open(
        "data/raw/telegram_messages/2026-06-28/chemed.json",
        "w"
    ) as f:
        json.dump(messages, f, indent=4)

with client:
    client.loop.run_until_complete(scrape("CheMed123"))
