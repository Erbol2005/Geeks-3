import asyncio
import logging
import os
import random

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from aiogram.filters import Command




load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}")


@dp.message(Command("random_pic"))
async def send_random_pic(message: types.Message):
    images_list = ['1.webp', '2.webp', '3.webp', '4.webp', 'i.webp']
    images_dir = "images/"

    random_image = random.choice(images_list)
    image_path = os.path.join(images_dir, random_image)

    file = types.FSInputFile(image_path)
    await message.answer_photo(
        photo=file,
    )


@dp.message(Command("my_info"))
async def my_info(message: types.Message):
    await message.reply(
        f'''
        Ваш ID: {message.from_user.id}\n 
        Ваше имя: {message.from_user.first_name}\n
        Ваше пользовательское имя: {message.from_user.username}\n
        '''
    )


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="my_info", description="Моя информация"),
        types.BotCommand(command="random_pic", description="Случайная картинка")
    ])

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
