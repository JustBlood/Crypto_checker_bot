from aiogram.dispatcher.filters.state import StatesGroup, State


class EnterCrypto(StatesGroup):
    inputing_crypto = State()
    continue_menu = State()

class CheckCryptoNow(StatesGroup):
    inputing_crypto = State()
    continue_menu = State()