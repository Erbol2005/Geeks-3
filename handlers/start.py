from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(url="https://www.google.kg/maps/place/Аниме+магазинчик", text="Наш адрес"),
                types.InlineKeyboardButton(url="https://instagram.com/", text="Наш инстаграм"),
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about"),
            ]
        ]
    )
    await message.answer(
        f"""Здравствйте, {message.from_user.full_name}. Мы аниме магазин, с разнообразным асортиментом. 
        """, reply_markup=kb
    )


@start_router.callback_query(F.data == "about")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer("Добро пожаловать в мир аниме!"
                                  "Магазин, где вы найдете лучшие предметы коллекционирования,"
                                  "фигурки персонажей и многое другое, вдохновленное японской анимацией. "
                                  "Присоединяйтесь к нам и откройте новые грани аниме культуры!"
                                  )