import asyncio
import logging

import aiogram

from src.config import config
from src.handlers import router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    bot = aiogram.Bot(token=config.BOT_TOKEN)
    dispatcher = aiogram.Dispatcher()
    dispatcher.include_routers(router)
    try:
        logger.info("Starting polling...")
        await dispatcher.start_polling(bot)
    except Exception:
        logger.exception("Failed to start polling")


if __name__ == "__main__":
    asyncio.run(main())
