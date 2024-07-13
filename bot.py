import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_reader import config
import other_handlers, user_handlers

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(level=logging.INFO)
    logger.info('Starting bot...')
    bot = Bot(token=config.bot_token.get_secret_value(),
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())