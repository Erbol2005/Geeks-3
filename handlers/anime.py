from aiogram import Router, F, types
from aiogram.filters import Command

from db.queries import get_anime, get_stationery, get_figures


anime_router = Router()

@anime_router.message(Command("assortment"))
async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="figures"),
            ],
            [
                types.KeyboardButton(text="stationery"),
                types.KeyboardButton(text="random_anime"),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите категорию товаров:", reply_markup=kb)

@anime_router.message(F.text.lower() == "figures")
async def figures(message: types.Message):
    figures_list = get_figures()
    kb = types.ReplyKeyboardRemove()
    await message.answer("Фигурки персонажей из игр и манги!", reply_markup=kb)
    for figur in figures_list:
        await message.answer(f"Название{figur[1]}, Высота: {figur[2]}, Фото: {figur[3]}\n")


@anime_router.message(F.text.lower() == "stationery")
async def stationery(message: types.Message):
    stationers_list = get_stationery()
    kb = types.ReplyKeyboardRemove()
    await message.answer("Канцелярские товары, которые делают рабочее пространство ярче и веселее.", reply_markup=kb)
    for stationers in stationers_list:
        await message.answer(f"{stationers[1]}, Количество: {stationers[2]}, Наличие: {stationers[3]}\n")


@anime_router.message(F.text.lower() == "random_anime")
async def random_anime(message: types.Message):
    anime_list = get_anime()
    kb = types.ReplyKeyboardRemove()
    await message.answer("Вот три случайных аниме и их продолжительность:\n", reply_markup=kb)
    for anime in anime_list:
        await message.answer(f"Название: {anime[1]}, Эпизоды: {anime[2]}, Продолжительность: {anime[3]}\n")
