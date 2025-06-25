from pyrogram import Client, filters
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client("ClassyBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("🎬 Hello! I’m your Classy Movie Bot! Type any movie name to begin.")

@bot.on_message(filters.text & filters.private)
def movie_search(client, message):
    query = message.text.lower()
    if "kgf" in query:
        message.reply_text("🔗 KGF Link: https://t.me/YourMovieChannel/123")
    elif "rrr" in query:
        message.reply_text("🔗 RRR Link: https://t.me/YourMovieChannel/456")
    else:
        message.reply_text("❌ Movie not found.")

bot.run()
