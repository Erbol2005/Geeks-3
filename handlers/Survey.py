from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext



survey_shop = Router()

class Survey(StatesGroup):
    name = State()
    age = State()
    favorite_anime = State()
    favorite_character = State()

@survey_shop.message(Command("survey"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(Survey.name)
    await message.answer("Привет! Как тебя зовут?")

@survey_shop.message(Command("stop"))
@survey_shop.message(F.text == "stop")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Опрос прекращен.")

@survey_shop.message(Survey.name)
async def process_name(message: types.Message, state: FSMContext):
    if len(message.text) < 3:
        await message.answer("Слишком короткое имя")
    else:
        await state.update_data(name=message.text)
        await message.answer(f"Спасибо, {message.text}!")

        await state.set_state(Survey.age)
        await message.answer("Сколько тебе лет? (Ответь цифрой)")

@survey_shop.message(Survey.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Пожалуйста, вводи только цифры")
    elif int(age) < 1 or int(age) > 100:
        await message.answer("Пожалуйста, вводи корректный возраст (от 1 до 100).")
    else:
        await state.update_data(age=int(age))
        await state.set_state(Survey.favorite_anime)
        await message.answer("Какое твое любимое аниме?")

@survey_shop.message(Survey.favorite_anime)
async def process_favorite_anime(message: types.Message, state: FSMContext):
    await state.update_data(favorite_anime=message.text)
    await state.set_state(Survey.favorite_character)
    await message.answer("Кто твой любимый персонаж из аниме?")

@survey_shop.message(Survey.favorite_character)
async def process_favorite_character(message: types.Message, state: FSMContext):
    await state.update_data(favorite_character=message.text)

    data = await state.get_data()
    await message.answer("Спасибо за участие в опросе!")
    await message.answer(f"Имя: {data['name']}\n"
                         f"Возраст: {data['age']}\n"
                         f"Любимое аниме: {data['favorite_anime']}\n"
                         f"Любимый персонаж: {data['favorite_character']}")

    await state.finish()