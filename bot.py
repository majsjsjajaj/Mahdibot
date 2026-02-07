import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

VIDEO_MAP = {
    "vid1": "AAMCAQADGQECxa99aYbDTHURPoZRKBYPsnDz8QN7KI0AAgkHAAIoLDlEYaULZhPyyecBAAdtAAM6BA",
    "vid2": "AAMCAQADGQECxa93aYbDRKECjf7xmkxb5QM_CfsWFaIAAggHAAIoLDlElkxZBYQDVFsBAAdtAAM6BA",
    "vid3": "AAMCAQADGQECxa8eaYbDImEx9HLnmVWYc0IKnSFCNkQAAgcHAAIoLDlEXJ3qC0zRtQ4BAAdtAAM6BA",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ رابط غير صالح")
        return

    code = context.args[0]
    video_id = VIDEO_MAP.get(code)

    if not video_id:
        await update.message.reply_text("❌ هذا الرابط غير معروف")
        return

    msg = await update.message.reply_video(video=video_id)

    await asyncio.sleep(15)
    await msg.delete()

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
