from aiogram import types, Dispatcher
from create_bot import bot
from data_base import sqlite_db
from keyboards import kb_main

async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Здарова. Этот бот поможет тебе контролировать время которое ты тратишь на игры.\n'
                           '/moder - команда для добавления в список новой игры или удаления старой (Всего может быть 10 игр)\n'
                           '/game_start - команда для начала выбора игры и отсчета таймера\n'
                           '/menu - команда для просмотра добавленных игр и оставшегося времени\n'
                           '/help - команда для вывода команд бота\n'
                           '*Если вдруг бот долго не реагирует на что-то, значит он умер или ожидает иного действия',
                           reply_markup=kb_main.button_case_add)
    await message.delete()


async def menu(message: types.Message):
    menu = await sqlite_db.sql_read_menu(message)
    if len(menu) > 0:
        for ret in menu:
            await bot.send_message(message.from_user.id, f'{ret[2]}:  {ret[3]}  /  {ret[4]}')
    else:
        await bot.send_message(message.from_user.id, 'Для начала необходимо добавить игры нажав "/moder"')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(menu, commands=['menu'])
