from aiogram.types import CallbackQuery as cq
from data import dp, bot
from aiogram import Dispatcher
from other.keyboards import faq_keyboard, back_keyboard
# @dp.callback_query(lambda callback_query: callback_query.data == 'main_corps' or callback_query.data == 'Назад')
async def show_map(callback_query: cq):
        await bot.send_message(callback_query.from_user.id, f'Первый корпус:\n улица Артёма, 9, Сургут, Ханты-Мансийский автономный округ, 628404\n')
        await bot.send_location(callback_query.from_user.id, 61.255528, 73.402754)
        await bot.send_message(callback_query.from_user.id, f'Второй корпус:\nулица 50 лет ВЛКСМ, 10/2, Сургут, Ханты-Мансийский автономный округ, 628417\n')
        await bot.send_location(callback_query.from_user.id, 61.256918, 73.357482,)

 
def register_handlers_coprs(dp: Dispatcher):
    dp.callback_query.register(show_map, lambda callback_query: callback_query.data == 'main_corps' or callback_query.data == 'Назад')