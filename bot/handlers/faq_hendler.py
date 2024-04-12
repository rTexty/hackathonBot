from aiogram import Dispatcher
from aiogram.types import CallbackQuery as cq
from data import  bot
from other.keyboards import faq_keyboard,back_keyboard




# @dp.callback_query(lambda callback_query: callback_query.data == 'Назад' or callback_query.data == 'main_info')
async def FAQ(callback_query: cq):
    if callback_query.data == 'main_info':
        await bot.send_message(callback_query.from_user.id, f'Ниже представлены часто задаваемые вопросы(FAQ):\n', reply_markup=faq_keyboard)
    elif callback_query.data == 'Назад':
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)

# @dp.callback_query(lambda callback_query: callback_query.data == 'live_corps' or callback_query.data == 'Назад')
async def live_corps(callback_query: cq):
    if callback_query.data == 'live_corps':
        await bot.send_message(callback_query.from_user.id, f"В распоряжении Сургутского государственного педагогического Университета имеются два благоустроенных студенческих общежития квартирного типа.\n\nОбщежития для студентов и сотрудников расположены по адресам:\nг. Сургут, ул.50 лет ВЛКСМ, д. 2/2;\nг. Сургут, ул.30 лет Победы, д. 60/1", reply_markup=back_keyboard)
        await bot.send_photo(callback_query.from_user.id, 'bot/img/coprs.png')
    elif callback_query.data == 'Назад':
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    
# @dp.callback_query(lambda callback_query: callback_query.data == 'count_corps' or callback_query.data == 'Назад')
async def count_corps(callback_query: cq):
    if callback_query.data == 'count_corps':
        await bot.send_message(callback_query.from_user.id, f"Учебный корпус № 1 расположен по адресу: \nг. Сургут, ул. 50 лет ВЛКСМ, д. 10/2\n\nУчебный корпус № 2 — расположен по адресу: \nг. Сургут, ул. Артёма, д. 9;\n\nКонцертно-спортивный комплекс (КСК) — расположен по адресу: \nг. Сургут, ул. Артёма, д. 9.",reply_markup=back_keyboard)
    elif callback_query.data == 'Назад':
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)

async def stipend(callback_query: cq):
    if callback_query.data == 'stipendia':
        await bot.send_message(callback_query.from_user.id, f'Государственная академическая стипендия студента в СурГПУ - 7 600. До первой сессии ее получают все первокурсники-бюджетники. А уже по итогам промежуточной аттестации на стипендию традиционно могут рассчитывать только те обучающиеся, которые сдали экзамены без троек. Кроме того, студенты могут получить и повышенную стипендию. По данным пресс-службы СурГПУ, такая стипендия назначается студентам со второго курса за достижения в учебной, научно-исследовательской, общественной и спортивной деятельности.\n\nЕсли достижения в одной области, то со второго курса студенты получат 9500 рублей, с 3-5 курса – 9880 рублей. При достижениях в нескольких областях деятельности размер выплаты ежемесячно составит от 11 400 до 12160 рублей', reply_markup=back_keyboard)
    elif callback_query.data == 'Назад':
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)

def register_handlers_faq(dp: Dispatcher):
    dp.callback_query.register(FAQ, lambda callback_query: callback_query.data == 'Назад' or callback_query.data == 'main_info')
    dp.callback_query.register(live_corps, lambda callback_query: callback_query.data == 'live_corps' or callback_query.data == 'Назад')
    dp.callback_query.register(count_corps, lambda callback_query: callback_query.data == 'count_corps' or callback_query.data == 'Назад')
    dp.callback_query.register(stipend, lambda callback_query: callback_query.data == 'stipendia' or callback_query.data == 'Назад')