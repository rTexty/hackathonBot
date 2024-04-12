from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(callback_data="Назад", text="Назад", )
        ]
    ]
)


levels_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Бакалавриат', callback_data='Бакалавриат')],
        [InlineKeyboardButton(text='Магистратура', callback_data='Магистратура')],
        [
        InlineKeyboardButton(text='Аспирантура', callback_data='Аспирантура'),
        ]
    ]
)

directions_bakalavr = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Математика и Информатика', callback_data='math_info')
        ],
        [
            InlineKeyboardButton(text='Математика и Физика', callback_data='math_physics'),
        ]
    ]
)

directions_magistr = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Цифровизация образования: проектирование, сопровождение, экспертиза ', callback_data='mag_edu')],
    ]
)
directions_aspir = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Методология и технология профессионального образования', callback_data='aspir_edu')
        ],
        [
            InlineKeyboardButton(text='Общая педагогика, история педагогики и образования', callback_data='aspir_history'),
        ]
    ]
)