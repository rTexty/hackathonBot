from data import dp,bot
from aiogram.types import CallbackQuery as cq
from other.texts import *
from other.keyboards import levels_keyboard, back_keyboard
from aiogram import Dispatcher


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
                    

async def study_process(callback_query: cq):
    if callback_query.data == 'std':
        await callback_query.answer(text=f"Вы выбрали {callback_query.data}")
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(chat_id=callback_query.from_user.id, text="Выберите уровень образования:", reply_markup=levels_keyboard)
    elif callback_query.data == 'Назад':
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    
def register_handlers_edu(dp: Dispatcher):
    dp.callback_query.register(study_process, lambda callback_query: callback_query.data == 'std' or callback_query.data == 'Назад')
    dp.callback_query.register(process_service, lambda callback_query: callback_query.data)