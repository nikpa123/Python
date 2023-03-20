from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from operations import *

b1 = KeyboardButton('+', sum_value(num1, num2))
b2 = KeyboardButton('-', diff_value(num1, num2))
user_kb = ReplyKeyboardMarkup(resize_keyboard=True)
user_kb.row(b1, b2)