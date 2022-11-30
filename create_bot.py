from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from additional_functions.get_from_env_function import get_from_env


storage = MemoryStorage()


bot = Bot(token=get_from_env("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher(bot, storage=storage)


