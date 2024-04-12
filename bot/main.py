from aiogram import Bot, Dispatcher
from bot.keyboards import levels_keyboard, back_keyboard
from bot.config import token
from aiogram.filters import CommandStart
import logging
import asyncio
from aiogram.types import CallbackQuery as cq
from bot.texts import *
from bot.logic import *


bot = Bot(token=token)

dp = Dispatcher()


"""
Приветственное сообщение
"""
@dp.message(CommandStart)
async def start(message):
    await message.answer(f"Привет, {message.from_user.full_name}!\nЯ бот-помощник СурГПУ, который поможет вам поступить в университет.")
    await bot.send_message(chat_id=message.from_user.id, text="Выберите уровень образования:", reply_markup=levels_keyboard)


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
        message = await bot.send_message(callback_query.from_user.id, f"Для поступления на {selected_text}, необходимо {levels[selected_text]}\n{text}", reply_markup=markup)
        messages_to_delete.append(message.message_id)
    elif callback_query.data == 'Назад':
        # Удаление всех сообщений из списка
        await delete_messages(bot, callback_query.from_user.id)
    elif callback_query.data in info_dict.keys():
        # Получение информации на основе выбранного ключа
        info = info_dict.get(callback_query.data)
        link = link_dict.get(callback_query.data)

        if info:
            if link:
                # Отправка сообщения с информацией и добавление его идентификатора в список для последующего удаления
                info_message = await bot.send_message(callback_query.from_user.id, f"Вступительные испытания для поступления на {selected_text}:\n\n{info}\n\nБолее подробная информация на сайте: https://www.surgpu.ru/Abitur/{link}/", reply_markup=back_keyboard)
                messages_to_delete.append(info_message.message_id)



async def main() -> None:
    bot = Bot(token=token,)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
