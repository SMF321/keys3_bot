import logging

from aiogram import Dispatcher

from data.config import ADMINS

from utils.db_api.main import GET_ID

async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен\n/start")

        except Exception as err:
            logging.exception(err)
    for user in GET_ID():
        try:
            await dp.bot.send_message(user, "Бот Запущен\n/start")

        except Exception as err:
            logging.exception(err)