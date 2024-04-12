from aiogram import Dispatcher
from data import dp,bot
from aiogram.filters import CommandStart
from other.keyboards import main_keyboard

async def start(message):
    await message.answer(f"Привет, {message.from_user.full_name}!\nЯ бот-помощник СурГПУ, который поможет вам поступить в университет.")
    await bot.send_message(chat_id=message.from_user.id, text="С чего начнем?:", reply_markup=main_keyboard)

def register_start(dp: Dispatcher):
    dp.message.register(start, CommandStart())