import asyncio
import logging
from aiogram import Bot, Dispatcher, types

# Tokeningizni saqlab qoldim
API_TOKEN = '8490179708:AAEFgO2e3eYLfP4cb7H2SeXuVfJiXZEDyBc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Yangi versiyada filterlar shunday yoziladi
@dp.chat_join_request()
async def accept_request(update: types.ChatJoinRequest):
    try:
        await update.approve()
        print(f"Qabul qilindi: {update.from_user.full_name}")
    except Exception as e:
        print(f"Xato yuz berdi: {e}")

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot to'xtatildi")