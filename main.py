import misc
import handlers

#from handlers import setup

import asyncio
import logging

import asyncio
import logging

from aiogram import Bot, Dispatcher, types #del types
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

#from aiogram.utils import executor # del

import config
from handlers import router

from aiogram import Router

async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    #dp.include_router(router)
    dp.include_router(handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

async def main():
    await misc.bot.delete_webhook(drop_pending_updates=True)
    await misc.dp.start_polling(misc.bot, allowed_updates=misc.dp.resolve_used_update_types())

###
# async def feed_update(update: dict[str, any]) -> None: # Dict Any
#     telegram_update = types.Update(**update)
#     dp = Dispatcher(storage=MemoryStorage()) ###
#     dp.include_router(router) ###
#     await dp.feed_webhook_update(Bot, telegram_update) # bot
###


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
