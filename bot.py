import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, WebAppInfo

WEBAPP_URL = "https://yotsuki-taylor.github.io/RoadMovie/"


def build_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Play", web_app=WebAppInfo(url=WEBAPP_URL))],
        ],
        resize_keyboard=True,
        one_time_keyboard=False,
        selective=False,
    )


async def start_handler(message: Message) -> None:
    await message.answer("Нажми кнопку Play, чтобы открыть Web App.", reply_markup=build_keyboard())


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "Не задан токен бота. Установи переменную окружения BOT_TOKEN и запусти снова."
        )

    bot = Bot(token=token)
    dp = Dispatcher()

    dp.message.register(start_handler, CommandStart())

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

