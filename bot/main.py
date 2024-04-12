from aiogram import F, Bot, Dispatcher
from keyboards import levels_keyboard, back_keyboard, main_keyboard
from config import token
from aiogram.filters import CommandStart
import logging
import asyncio
from aiogram.types import CallbackQuery as cq
from texts import *


bot = Bot(token=token)

dp = Dispatcher()


"""
Приветственное сообщение
"""
@dp.message(CommandStart)
async def start(message):
    await message.answer(f"Привет, {message.from_user.full_name}!\nЯ бот-помощник СурГПУ, который поможет вам поступить в университет.")
    await bot.send_message(chat_id=message.from_user.id, text="С чего начнем?:", reply_markup=main_keyboard)

@dp.callback_query(lambda callback_query: callback_query.data == 'std' or callback_query.data == 'Назад')
async def study_process(callback_query: cq):
    """
    Asynchronous callback function for handling study process.
    
    Parameters:
    - callback_query: The callback query object
    
    Return Type: None
    """
    if callback_query.data == 'std':
        await callback_query.answer(text=f"Вы выбрали {callback_query.data}")
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(chat_id=callback_query.from_user.id, text="Выберите уровень образования:", reply_markup=levels_keyboard)
    elif callback_query.data == 'Назад':
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    

@dp.callback_query(lambda callback_query: callback_query.data == 'main_corps' or callback_query.data == 'Назад')
async def show_map(callback_query: cq):
    await bot.send_message(callback_query.from_user.id, f'Первый корпус:\n улица Артёма, 9, Сургут, Ханты-Мансийский автономный округ, 628404\n')
    await bot.send_location(callback_query.from_user.id, 61.255528, 73.402754)
    await bot.send_message(callback_query.from_user.id, f'Второй корпус:\nулица 50 лет ВЛКСМ, 10/2, Сургут, Ханты-Мансийский автономный округ, 628417\n')
    await bot.send_location(callback_query.from_user.id, 61.256918, 73.357482)



"""
Обрабатывает сервис на основе обратного вызова.

Параметры:
- callback_query (cq): Объект обратного вызова.

Эта функция обрабатывает обратный вызов путем извлечения данных, поиска соответствующей кнопки,
обработки различных сценариев на основе данных обратного вызова и отправки соответствующих сообщений.
"""

@dp.callback_query(lambda callback_query: callback_query.data)
async def process_service(callback_query: cq):
        # Извлечение данных обратного вызова из объекта обратного вызова
        callback_data = callback_query.data

        await callback_query.answer(text=f"Вы выбрали {callback_data}")
        await bot.answer_callback_query(callback_query.id)

        # Поиск кнопки с совпадающими данными обратного вызова и извлечение ее текста
        global selected_text
        for row in levels_keyboard.inline_keyboard:
            for button in row:
                if button.callback_data == callback_data:
                    selected_text = button.text
                    break
            else:
                continue
            break
        if callback_query.data in messages:
            markup, text = messages[callback_query.data]
            await bot.send_message(callback_query.from_user.id, f"Для поступления на {selected_text}, необходимо {levels[selected_text]}\n{text}", reply_markup=markup)
        elif callback_query.data == 'Назад':
            await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        elif callback_query.data in info_dict.keys():
            # Получение информации на основе выбранного ключа
            info = info_dict.get(callback_query.data)
            link = link_dict.get(callback_query.data)

            if info:
                if link:
                    # Отправка сообщения с информацией и добавление его идентификатора в список для последующего удаления
                    await bot.send_message(callback_query.from_user.id, f"Вступительные испытания для поступления на {selected_text}:\n\n{info}\n\nБолее подробная информация на сайте: https://www.surgpu.ru/Abitur/{link}/", reply_markup=back_keyboard)
                    


async def main() -> None:
    bot = Bot(token=token,)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
