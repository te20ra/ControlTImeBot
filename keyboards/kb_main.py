from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
button_mod = KeyboardButton('/moder')
button_start_game = KeyboardButton('/game_start')
button_menu = KeyboardButton('/menu')
button_help = KeyboardButton('/help')


button_case_add = ReplyKeyboardMarkup(resize_keyboard=True).insert(button_mod).insert(button_start_game).add(button_help).insert(button_menu)