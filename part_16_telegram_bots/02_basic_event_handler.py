import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

BOT_TOKEN = "6447680509:AAFtZP4lzes4DdrpEpvDEk8EVkx5iYK3Cgk"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def answer_as_echo(message: types.Message):
    await message.answer(text=message.text)


@dp.message()
async def reply_as_echo(message: types.Message):
    await message.reply(text=message.text)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
