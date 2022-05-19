from aiogram import types

""" 
Инициализируем клавиатуру на 2 состояние бота при выдаче базы данных о крипте
кнопка 1 - выбрать ещё одну крипту -> относит на 1 состояние (выбор крипты)
кнопка 2 - вернуться в главное меню -> завершает состояние и возвращает главное меню

"""


continue_kb = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton('🟡 Выбрать ещё одну криптовалюту'),
            types.KeyboardButton('⚪ Вернуться в главное меню')
        ]
    ]
    ,
    resize_keyboard=True
)

CONTINUE_KB_BUTTONS = [continue_kb.keyboard[i][j]['text'] for i in range(len(continue_kb.keyboard)) for j in range(len(continue_kb.keyboard[0]))]