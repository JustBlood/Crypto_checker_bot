from aiogram import types

from keyboards.default import continue_kb
from loader import dp
from parsing.crypto_parser_1 import parser_1
from states import CheckCryptoNow

import logging
logging.basicConfig(level=logging.INFO)

@dp.message_handler(state=CheckCryptoNow.inputing_crypto)
async def parse_crypto_now(message: types.Message):
    curr_state = parser_1(message.text.upper())
    if curr_state == 'error empty result':
        logging.info(msg=f'Поиск крипты не удался. Текст сообщения: {message.text}')
        await message.answer('😣 Поиск не удался, скорее всего Вы неправильно ввели название криптовалюты...', reply_markup=continue_kb)
    elif curr_state == 'error status code':
        logging.info(msg=f'Поиск крипты не удался, сайт крипты не ответил. Текст сообщения: {message.text}')
        await message.answer('🚧 Техническая ошибка. Криптобиржа недоступна.')
    elif type(curr_state) == dict:
        logging.info('Текущий курс криптовалюты успешно возвращен')
        await message.answer(f"💰 Криптовалюта {message.text.upper()} сейчас продается по цене: {curr_state['close']}", reply_markup=continue_kb)
    else:
        await message.answer('Непредвиденная ошибка.')
    await CheckCryptoNow.continue_menu.set()