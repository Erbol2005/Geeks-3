import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


@dp.message(Command("png"))
async def send_pic(messange: types.Message):
    photo = types.FSInputFile("png/i.webp")
    await messange.answer_photo(
        photo=photo,
        caption="Котик"
    )

@dp.message(Command=['myinfo'])
async def my_info(message: types.Message):
    user_info = (
        f"Ваш ID: {message.from_user.id}\n"
        f"Ваше имя: {message.from_user.first_name}\n"
        f"Ваш никнейм: {message.from_user.username}"
    )
    await message.answer(user_info)

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"{message.text}, {message.from_user.first_name}")

async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="pic", description="Получить картинку")
    ])

    # запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())