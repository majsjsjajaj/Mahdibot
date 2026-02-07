import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

VIDEO_ID = "BAACAgEAAxkBAAIGTGmGqWWi2rLEUOcJgtzR_wTdIGN3AAJmBQACGuk4REeKcrzqTmD-OgQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_video(
        video=VIDEO_ID,
        caption="🎬 فيديو مؤقت"
    )

    await asyncio.sleep(15)
    await msg.delete()

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
