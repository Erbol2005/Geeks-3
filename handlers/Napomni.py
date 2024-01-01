from aiogram import Router, F, types
from aiogram.filters import Command
from Bot import bot, scheduler
from aiogram.fsm.context import FSMContext

napomni_router = Router()


@napomni_router.message(F.text.startswith("напомни"))
async def remaider(massage: types.Message):
    reminder_text = massage.text.removeprefix("напомни").strip()
    scheduler.add_job(
        send_remaider,
        trigger='interval',
        seconds = 5,
        kwargs = {"chat_id": massage.from_user.id, "text": reminder_text}
    )


@napomni_router.message(Command("stop"))
@napomni_router.message(F.text == "stop")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Напоминание прекращено.")


async def send_remaider(chat_id: int, text: str):
    await bot.send_message(
        chat_id = chat_id,
        text = f"Напоминаю: {text}"
    )
