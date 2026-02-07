import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

def load_posts():
    with open("posts.txt", "r", encoding="utf-8") as f:
        return f.read().splitlines()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    posts = load_posts()
    for post in posts:
        msg = await update.message.reply_text(post)
        await asyncio.sleep(15)
        await msg.delete()

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()