from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import main_kb
from loader import dp
from states import EnterCrypto, CheckCryptoNow

@dp.message_handler(state=EnterCrypto.continue_menu)
async def get_crypto_file(message: types.Message, state: FSMContext):
    """Тут происходит парсинг крипты и отправка файла её данных"""
    if message.text == '🟡 Выбрать ещё одну криптовалюту':
        await message.answer('Введите название криптовалюты:', reply_markup=types.ReplyKeyboardRemove())
        await EnterCrypto.inputing_crypto.set()
        return
    elif message.text == '⚪ Вернуться в главное меню':
        await message.answer('Операция завершена, спасибо за использование 😊',reply_markup=main_kb)
    else:
        await message.answer('🥺 Увы, комманда не распознана. Возвращаю в главное меню...',reply_markup=main_kb)
    await state.finish()

@dp.message_handler(state=CheckCryptoNow.continue_menu)
async def get_crypto_file(message: types.Message, state: FSMContext):
    """Тут происходит парсинг крипты и отправка файла её данных"""
    if message.text == '🟡 Выбрать ещё одну криптовалюту':
        await message.answer('Введите название криптовалюты:', reply_markup=types.ReplyKeyboardRemove())
        await CheckCryptoNow.inputing_crypto.set()
        return
    elif message.text == '⚪ Вернуться в главное меню':
        await message.answer('Операция завершена, спасибо за использование 😊',reply_markup=main_kb)
    else:
        await message.answer('🥺 Увы, комманда не распознана. Возвращаю в главное меню...',reply_markup=main_kb)
    await state.finish()