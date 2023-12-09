import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
import logging

BOT_TOKEN = "6882174935:AAFBW-hD9Smw5vLGWk3lnxY4UIZtVCYQPc0"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("png"))
async def send_pic(messange: types.Message):
    photo = types.FSInputFile("png/i.webp")
    await messange.answer_photo(
        photo=photo,
        caption="Котик"
    )

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"{message.text}, {message.from_user.first_name}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())