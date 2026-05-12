import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiohttp import web



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



async def handle(request):
    return web.Response(text="Bot is running!")

async def on_startup(dispatcher: Dispatcher):
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.getenv("PORT", 8080)))
    await site.start()

# Dispatcher-ni ishga tushirayotganda on_startup-ni bog'lang
# Masalan: await dp.start_polling(bot, on_startup=on_startup)