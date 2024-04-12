
messages_to_delete = []
# Функция для удаления всех сообщений из списка
async def delete_messages(bot, chat_id):
    for message_id in messages_to_delete:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
    messages_to_delete.clear()
