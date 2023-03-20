import asyncio
from handlers import dp
from aiogram.utils import executor
import platform
if platform.system() == 'Windows':
   asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
async def start_bot(_):
    print('Бот запущен')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
