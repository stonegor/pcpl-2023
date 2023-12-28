import asyncio

from aiogram import Bot, Dispatcher
from core.config import load_config
from core.router import router


async def main():
    config = load_config()

    bot = Bot(config.telegram.token, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
