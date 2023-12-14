import random
from aiogram import Router, types
from aiogram.filters import Command
import os

pic_router = Router()
@pic_router.message(Command("random_pic"))
async def send_random_pic(message: types.Message):
    images_list = ['1.webp', '2.webp', '3.webp', '4.webp', 'i.webp']
    images_dir = "images/"

    random_image = random.choice(images_list)
    image_path = os.path.join(images_dir, random_image)

    file = types.FSInputFile(image_path)
    await message.answer_photo(
        photo=file,
    )