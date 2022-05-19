import logging

from aiogram import types

from DB_work.get_db_names import get_db_names
from keyboards.default import main_kb, MAIN_KB_BUTTONS
from states import EnterCrypto, CheckCryptoNow
from loader import dp

@dp.message_handler(text=[button for button in MAIN_KB_BUTTONS])
async def handler_messages(message: types.Message):
    """Здесь происходит обработка всех внутренних комманд бота"""

    '''1-4 комманды'''
    logging.info('Была введена команда из меню')
    if message.text == main_kb.keyboard[0][0]['text']:
        all_names = get_db_names()
        await message.answer(text='💱 Все криптовалюты, находящиеся в базе данных:\n' + all_names)
    elif message.text == main_kb.keyboard[0][1]['text']:
        await message.answer('❓ Введите название криптовалюты:', reply_markup=types.ReplyKeyboardRemove())
        await EnterCrypto.inputing_crypto.set()
    elif message.text == main_kb.keyboard[1][0]['text']:
        await message.answer('❓ Введите название криптовалюты:', reply_markup=types.ReplyKeyboardRemove())
        await CheckCryptoNow.inputing_crypto.set()
    elif message.text == main_kb.keyboard[1][1]['text']:
        pass