from aiogram import types
from loader import dp

import logging
logging.basicConfig(level=logging.INFO)

@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    logging.info('Введена команда /help')
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'Всё просто, у бота всего 1 рабочая команда,\n'
                         f'Для старта работы бота введи /start\n')