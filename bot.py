from telegram.ext import Application, MessageHandler, filters
import os

TOKEN = os.getenv("TOKEN")

async def get_id(update, context):
    if update.message.video:
        await update.message.reply_text(
            f"FILE_ID:\n{update.message.video.file_id}"
        )

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.VIDEO, get_id))
app.run_polling()
