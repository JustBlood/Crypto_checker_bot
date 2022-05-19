from aiogram import types
from aiogram.dispatcher import FSMContext

from DB_work.get_db_names import get_db_names
from DB_work.get_crypto import save_crypto_data_in_file
from keyboards.default.keyboard_continue_menu import continue_kb
from loader import dp
from states import EnterCrypto

from parsing.crypto_parser_60 import main_parser_60

@dp.message_handler(state=EnterCrypto.inputing_crypto)
async def get_crypto_file(message: types.Message, state: FSMContext):
    """Тут происходит парсинг крипты и отправка файла её данных"""

    if message.text.lower() in get_db_names().lower():
        await message.answer('🔎 Информация успешно найдена, подготавливается csv файл...')
        save_crypto_data_in_file(message)
    else:
        await message.answer('⏳ Данных нет в базе, читаем новые данные, ожидайте в течение 1 минуты...')
        status = main_parser_60(message.text.upper())
        if status == 'success':
            await message.answer('🔎 Информация успешно найдена, подготавливается csv файл...')
            save_crypto_data_in_file(message)
        else:
            await message.answer('😔 Данной криптовалюты не существует.')
            await state.finish()
            return

    await message.answer_document(open(f'files_to_send/{message.text}.csv', 'rb'))
    await message.answer('Выберите действие.', reply_markup=continue_kb)
    await EnterCrypto.continue_menu.set()
