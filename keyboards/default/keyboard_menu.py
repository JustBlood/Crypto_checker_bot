from aiogram import types

""" 
Инициализируем основную клавиатуру при старте бота
кнопка 1 - имена всех криптовалют в базе
кнопка 2 - найти криптовалюту
кнопка 3 - Узнать текущий курс валюты по имени
кнопка 4 - Подробная информация о командах
"""


main_kb = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton('Крипта в базе'),
            types.KeyboardButton('Взять базу данных крипты по имени')
        ],
        [
            types.KeyboardButton('Узнать текущий курс крипты по имени'),
            types.KeyboardButton('Подробнее о командах')
        ]
    ]
    ,
    resize_keyboard=True
)

MAIN_KB_BUTTONS = [main_kb.keyboard[i][j]['text'] for i in range(len(main_kb.keyboard)) for j in range(len(main_kb.keyboard[0]))]