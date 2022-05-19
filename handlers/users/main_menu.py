import logging

import time

from aiogram import types

from DB_work.get_db_names import get_db_names
from keyboards.default import main_kb, MAIN_KB_BUTTONS
from states import EnterCrypto, CheckCryptoNow
from loader import dp

# Initialise logger_info
logging.basicConfig(level=logging.INFO)

@dp.message_handler(text=[button for button in MAIN_KB_BUTTONS])
async def handler_messages(message: types.Message):
    """Здесь происходит обработка всех внутренних комманд бота"""

    '''1-4 комманды'''
    logging.info('Была введена команда из главного меню')
    if message.text == main_kb.keyboard[0][0]['text']:
        logging.info(f'Выбрано действие {message.text}')
        all_names = get_db_names()
        await message.answer(text='💱 Все криптовалюты, находящиеся в базе данных:\n' + all_names)
    elif message.text == main_kb.keyboard[0][1]['text']:
        logging.info(f'Выбрано действие {message.text}')
        await message.answer('❓ Введите название криптовалюты:', reply_markup=types.ReplyKeyboardRemove())
        await EnterCrypto.inputing_crypto.set()
    elif message.text == main_kb.keyboard[1][0]['text']:
        logging.info(f'Выбрано действие {message.text}')
        await message.answer('❓ Введите название криптовалюты:', reply_markup=types.ReplyKeyboardRemove())
        await CheckCryptoNow.inputing_crypto.set()
    elif message.text == main_kb.keyboard[1][1]['text']:
        logging.info(f'Выбрано действие {message.text}')
        await message.answer('Сейчас я тебе всё поведаю, друг мой 😉')
        time.sleep(1)
        await message.answer('1️⃣ Команда (🟠 Крипта в базе) высылает тебе список всех доступных имён криптовалют, которые сейчас находятся в нашей базе данных\n\n'
                             '2️⃣ Команда (🟡 Взять базу данных крипты по имени) попросит ввести тебя название криптовалюты в валютной паре, т.е. по форме (КриптаВалюта).\n'
                             'Всё проще, чем кажется, это, например, BTCUSD или ETHUSDT\n'
                             'Далее я пришлю тебе файл формата Exel таблиц (csv) со всеми данными(интервал между записями 1 час)\n\n'
                             '3️⃣ Команда (🟢 Узнать текущий курс крипты по имени) также попросит тебя ввести название криптовалюты в валютной паре (см. 2️⃣ команду)\n'
                             'И далее пришлёт тебе текущий курс введённой криптовалюты\n\n'
                             '4️⃣ Команда (⚪ Подробнее о командах) представлена в этом сообщении 😄\n\n'
                             '✅ Вот и всё! Приятного пользования!\n(Ну же, скорее иди пробовать!)')