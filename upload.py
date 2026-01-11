import os
from pyrogram import Client

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
file = "backup.zip"

app = Client("uploader", api_id=api_id, api_hash=api_hash, bot_token=bot_token, in_memory=True)

with app:
    app.send_document(chat_id, file, caption="Database Backup")
