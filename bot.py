import os
import asyncio
from telegram import Bot

TOKEN = os.getenv("TOKEN")

async def main():
    bot = Bot(token=TOKEN)

    # إرسال رسالة تأكيد إن البوت اشتغل
    await bot.send_message(
        chat_id=1003025142,
        text="🤖 البوت اشتغل بنجاح على Railway!"
    )

    # خلي البوت شغال وما يطفي
    while True:
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
