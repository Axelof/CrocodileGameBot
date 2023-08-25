from aiogram import Bot, Dispatcher, enums
from aiogram.fsm.storage.memory import MemoryStorage

from settings import settings

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN, parse_mode=enums.ParseMode.HTML)
Bot.set_current(bot)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

from . import middlewares
from . import handlers
from . import callbacks