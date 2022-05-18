from aiogram import types
from aiogram.dispatcher import FSMContext

from DB_work.get_db_names import get_db_names
from DB_work.get_crypto import save_crypto_data_in_file
from loader import dp
from states import EnterCrypto

from parsing.crypto_parser import crypto_parser

@dp.message_handler(state=EnterCrypto.test1)
async def get_crypto_file(message: types.Message, state: FSMContext):
    """Тут происходит парсинг крипты и отправка файла её данных"""

    if message.text.lower() in get_db_names().lower():
        save_crypto_data_in_file(message)
    else:
        await message.answer('Данных нет в базе, читаем новые данные, ожидайте в течение 1 минуты...')
        status = crypto_parser(message.text.upper())
        if status == 'success':
            save_crypto_data_in_file(message)
        else:
            await message.answer('Данной криптовалюты не существует.')
            await state.finish()
            return

    await message.answer_document(open(rf'E:\prog\prog_py\parsing\Tolik_pr\files_to_send\{message.text}.txt'))

    await state.finish()