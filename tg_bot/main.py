import asyncio
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import Message
from keyboards import user_kb
import platform
if platform.system() == 'Windows':
   asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
   
bot = Bot("5653367283:AAHd-oHcSe_ZbPMBMvAWaTy9DSlzsmxZ2Fo")
dp = Dispatcher(bot)

num1 = ''
num2 = ''
old_value = ''
value = ''

async def on_start(_):
    print('Бот запущен')

@dp.message_handler(commands=['start'])
async def com_start(message: Message):
    await message.answer('Бот запущен и готов к работе')
    global value
    if value == '':
        await message.answer(message.from_user.id, '0', reply_markup=user_kb)
    else:
        await message.answer(message.from_user.id, value, reply_markup=user_kb)

# @dp.callback_query_handlers(func=lambda call: True)
# async def calculator(query):
#     global value, old_value
#     data = query.text
#
#     if data == '_':
#         pass
#     elif data == 'C':
#         value = ''
#     elif data == '<=':
#         if value != '':
#             value = value[:len(value)-1]
#     elif data == '=':
#         try:
#             value = str ( eval(value) )
#         except:
#             value = "Ошибка!"
#     else:
#         value += data
#
#     if  ( value != old_value and value != '' ) or ( '0' != old_value and value == ''):
#         if value == '':
#             bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=user_kb)
#             old_value = '0'
#         else:
#             bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=user_kb)
#     if value == "Ошибка!": value = ''

executor.start_polling(dp, skip_updates=True, on_startup=on_start)