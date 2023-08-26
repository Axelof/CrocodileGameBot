from aiogram import types
from aiogram.filters import Command

from telegram import dp


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Hello, world!"
    )
