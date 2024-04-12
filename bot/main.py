import logging
import asyncio
from data import dp,bot

from handlers import start_handler, edu_handler, faq_hendler, coprs_handler

start_handler.register_start(dp) 
faq_hendler.register_handlers_faq(dp)
coprs_handler.register_handlers_coprs(dp)
edu_handler.register_handlers_edu(dp)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
