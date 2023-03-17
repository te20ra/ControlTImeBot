from create_bot import sheduler
from aiogram import types, Dispatcher
from data_base import sqlite_db
from datetime import datetime


async def check_alarm(dp: Dispatcher, message: types.Message, id_sql, last_time):
    status = await sqlite_db.sql_status_check(id_sql)
    if status == 'sleep':
        sheduler.remove_job(f'alarm {id_sql}')
    elif status == 'active' and datetime.now() > last_time:
        await dp.bot.send_message(message.from_user.id, 'Заканчивай, ага')
