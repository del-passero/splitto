import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

# Проверяем, что всё есть!
if not BOT_TOKEN or not WEBAPP_URL:
    raise ValueError("Не заполнены переменные BOT_TOKEN и/или WEBAPP_URL в .env файле!")

# Настраиваем логирование (для отладки)
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Стартовая команда
@dp.message(CommandStart())
async def start(message: types.Message):
    # Кнопка для открытия WebApp
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="Открыть Splitto",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "👋 Привет! Это бот Splitto.\nНажми кнопку ниже, чтобы открыть приложение.",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
