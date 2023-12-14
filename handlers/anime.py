from aiogram import Router, F, types
from aiogram.filters import Command

anime_router = Router()

@anime_router.message(Command("assortment"))
async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="figures"),
                types.KeyboardButton(text="clothing"),
            ],
            [
                types.KeyboardButton(text="stationery"),
                types.KeyboardButton(text="other"),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите категорию товаров:", reply_markup=kb)

@anime_router.message(F.text.lower() == "figures")
async def figures(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Фигурки персонажей из аниме и манги - ваш любимый герой всегда рядом!", reply_markup=kb)

@anime_router.message(F.text.lower() == "clothing")
async def clothing(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Яркая одежда и аксессуары, вдохновленные миром аниме - стильно и уникально!", reply_markup=kb)

@anime_router.message(F.text.lower() == "stationery")
async def stationery(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Канцелярские товары, которые делают рабочее пространство ярче и веселее.", reply_markup=kb)

@anime_router.message(F.text.lower() == "other")
async def other(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Другие удивительные товары для настоящих фанатов аниме и манги.", reply_markup=kb)
