import aiogram
import asyncio



import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging


#Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Hello,{message.from_user.full_name}!')

    @dp.message(Command(commands=['stop']))
    async def start(message: types.Message):
        await message.answer(f'Hello,{message.from_user.full_name}!')

    async def main():
        await dp.start_polling(bot)
        if __name__ == '__main__':
           asyncio.run(main())


