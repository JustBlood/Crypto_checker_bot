from aiogram import types

from keyboards.default import continue_kb
from loader import dp
from parsing.crypto_parser_1 import parser_1
from states import CheckCryptoNow


@dp.message_handler(state=CheckCryptoNow.inputing_crypto)
async def parse_crypto_now(message: types.Message):
    curr_state = parser_1(message.text)
    if curr_state == 'error empty result':
        await message.answer('😣 Поиск не удался, скорее всего Вы неправильно ввели название криптовалюты...')
    elif curr_state == 'error status code':
        await message.answer('🚧 Техническая ошибка. Криптобиржа недоступна.')
    elif type(curr_state) == dict:
        await message.answer(f"💰 Криптовалюта {message.text} сейчас продается по цене: {curr_state['close']}", reply_markup=continue_kb)
    else:
        await message.answer('Непредвиденная ошибка.')
    await CheckCryptoNow.continue_menu.set()