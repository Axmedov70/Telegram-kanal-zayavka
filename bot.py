import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiohttp import web

# --- SOZLAMALAR ---
API_TOKEN = '8490179708:AAEFgO2e3eYLfP4cb7H2SeXuVfJiXZEDyBc'
PORT = int(os.environ.get("PORT", 8080)) # Render beradigan portni oladi

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# --- BOT LOGIKASI ---
@dp.chat_join_request()
async def accept_request(update: types.ChatJoinRequest):
    try:
        await update.approve()
        logging.info(f"Qabul qilindi: {update.from_user.full_name}")
    except Exception as e:
        logging.error(f"Xato yuz berdi: {e}")

# --- RENDER UCHUN VEB-SERVER (PORT MUAMMOSINI YECHISH) ---
async def handle(request):
    return web.Response(text="Bot is running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    logging.info(f"Web server {PORT}-portda ishga tushdi.")

# --- ASOSIY ISHGA TUSHIRISH ---
async def main():
    logging.info("Bot ishga tushmoqda...")
    
    # 1. Veb-serverni ishga tushiramiz
    await start_web_server()
    
    # 2. Botni polling rejimida yoqamiz
    # Eslatma: Web server va Bot birgalikda ishlashi uchun bitta loopda bo'lishi kerak
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot to'xtatildi")