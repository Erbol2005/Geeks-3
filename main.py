import asyncio
import logging
from aiogram import types
from Bot import bot, dp
from handlers import (
    start_router,
    anime_router,
    pic_router,
    survey_shop,
    echo_router
)


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="random_pic", description="Рандомная картинка"),
        types.BotCommand(command="assortment", description="Асортимент"),
        types.BotCommand(command="survey", description="Опрос")
    ])

    dp.include_router(start_router)
    dp.include_router(anime_router)
    dp.include_router(pic_router)
    dp.include_router(survey_shop)
    dp.include_router(echo_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
