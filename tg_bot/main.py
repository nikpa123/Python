import asyncio
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import Message
# from keyboards import user_kb
# from operations import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import platform
if platform.system() == 'Windows':
   asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
   
bot = Bot("5653367283:AAHd-oHcSe_ZbPMBMvAWaTy9DSlzsmxZ2Fo")
dp = Dispatcher(bot)

num1 = ''
num2 = ''
value = None
proc = ''
async def on_start(_):
    print('Бот запущен')
сlass Form(StatesGroup):
    peremennaya = State()
@dp.message_handler(commands=['start'])
async def com_start(message: Message):
    await message.answer('Бот запущен и готов к работе')
    await message.answer(text = 'Введите первое число: ')
    await calc(message)

async def calc(message: Message, value = None):
    try:
        global num1, num2
        if value == None:
            num1 = int(message.text)
        else:
            num1 = str(value)
        b1 = KeyboardButton('+')
        b2 = KeyboardButton('-')
        user_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        user_kb.row(b1, b2)

        await message.answer(text='Выберите операцию: ', reply_markup=user_kb)
    await bot.send_message(message.chat.id, 'Отправь свое сообщение:')

async def operation(message: Message):
    try:
        global proc
        proc = message.text
    await message.answer(text='Введите ещё одно число: ', reply_markup=ReplyKeyboardRemove)





executor.start_polling(dp, skip_updates=True, on_startup=on_start)