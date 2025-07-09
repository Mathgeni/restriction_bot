import asyncio
import logging

import aiogram
import logging


from src.config import config
from src.handlers import router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


async def main():
    bot = aiogram.Bot(token=config.BOT_TOKEN)
    dispatcher = aiogram.Dispatcher()
    dispatcher.include_routers(router)
    try:
        await dispatcher.start_polling(bot)
    except Exception:
        ...

if __name__ == "__main__":
    asyncio.run(main())
