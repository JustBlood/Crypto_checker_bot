import logging

from aiogram import types

from loader import dp


@dp.message_handler()
async def handler(message: types.Message):
    logging.info('Была введена неизвестная команда')
    await message.answer('Я не знаю данную комманду, прости...')