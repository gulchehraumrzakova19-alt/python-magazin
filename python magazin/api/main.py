# TOKEN = "8607089032:AAFQ2My8FS1FcMpT6F83TlzAlNCKoM2KN3M"
# WEB_APP_URL = "https://tiny-nougat-4cfce5.netlify.app/" 
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# BOT TOKENINGIZNI YOZING
TOKEN = "8607089032:AAFQ2My8FS1FcMpT6F83TlzAlNCKoM2KN3M" 
URL = "https://python-magazin-offe.vercel.app/python%20magazin/index.html"     

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="🛍 Do'konni ochish", web_app=WebAppInfo(url=URL))]
    ], resize_keyboard=True)
    
    await message.answer(f"Salom {message.from_user.first_name}!\nUlug'bek Pay do'koniga xush kelibsiz!", reply_markup=kb)

@dp.message(F.web_app_data)
async def handle_data(message: types.Message):
    await message.answer(f"Sizdan yangi xabar keldi:\n\n{message.web_app_data.data}\n\nAdmin tez orada bog'lanadi!")

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())