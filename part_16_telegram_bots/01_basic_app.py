import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

BOT_TOKEN = "6447680509:AAFtZP4lzes4DdrpEpvDEk8EVkx5iYK3Cgk"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Promise -> pending / fulfilled / rejected
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


# print(f"{__name__ = }")

if __name__ == "__main__":
    asyncio.run(main())

