from aiogram import types
from loader import dp
from keyboards.default import keyboard_menu

import logging
logging.basicConfig(level=logging.INFO)

@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    logging.info('Введена команда /start')
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'Ну что, приступим? Выбери действие в меню ниже:', reply_markup=keyboard_menu.main_kb)