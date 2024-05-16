import asyncio

from aiogram.types import message
from magic_filter import F

import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging
import random

#Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет,{message.from_user.full_name}!')


@dp.message(Command(commands=['stop']))
async def stop(message: types.Message):
    await message.answer(f'STOP,{message.from_user.full_name}!')


@dp.message(Command(commands=['info', 'Инфо']))
@dp.message(F.text.lower() == "инфо")
async def info(message: types.Message):
    number = random.randint(0, 100)
    await message.answer(f'Вывожу рандомное число,{number}!')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
