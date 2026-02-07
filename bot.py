import os
import asyncio
import random
from telegram.ext import Application, CommandHandler
from telegram import Update

TOKEN = os.getenv("TOKEN")

def load_videos():
    with open("posts.txt") as f:
        return [x.strip() for x in f if x.strip()]

async def start(update: Update, context):
    videos = load_videos()
    video_id = random.choice(videos)

    msg = await update.message.reply_video(
        video=video_id,
        caption="🎬 فيديو مؤقت"
    )

    await asyncio.sleep(15)
    await msg.delete()

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
