from aiogram.utils import executor
from create_bot import dp, sheduler
from data_base import sqlite_db
from handlers import addGAME, other, startgame
async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()



addGAME.register_handlers(dp)
other.register_handlers_client(dp)
startgame.register_handlers(dp)


sheduler.start()
sheduler.add_job(sqlite_db.sql_clear_spendtime, "cron", day="1-31", hour="00", minute="01")
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
