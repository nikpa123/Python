from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('_', call_back='no')
b2 = KeyboardButton('C', call_back='C')
b3 = KeyboardButton('<=', call_back='<=')
b4 = KeyboardButton('/', call_back='/')
b5 = KeyboardButton('7', call_back='7')
b6 = KeyboardButton('8', call_back='8')
b7 = KeyboardButton('9', call_back='9')
b8 = KeyboardButton('*', call_back='*')
b9 = KeyboardButton('4')
b10 = KeyboardButton('5')
b11 = KeyboardButton('6')
b12 = KeyboardButton('-')
b13 = KeyboardButton('1')
b14 = KeyboardButton('2')
b15 = KeyboardButton('3')
b16 = KeyboardButton('+')
b17 = KeyboardButton('_')
b18 = KeyboardButton('0')
b19 = KeyboardButton(',')
b20 = KeyboardButton('=')

user_kb = ReplyKeyboardMarkup(resize_keyboard=True)

user_kb.row(b5, b6, b7, b8).row(b9, b10, b11, b12).row(b13, b14, b15, b16).row(b17, b18, b19, b20)