from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

# Создаем бота, где Bot(token='Токен вашего бота')
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# Создаем диспетчер
dp = Dispatcher(bot=bot, storage=MemoryStorage())