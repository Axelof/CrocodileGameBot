import asyncio

from settings import settings
from telegram import dp, bot

from loguru import logger


WEBHOOK_PATH = f'webhook/{settings.TELEGRAM_BOT_TOKEN}'


async def on_startup():
    # TODO: заменить polling с вебхуком на ngrok
    if settings.DEBUG:
        # не использовать await, т.к. это стопит сервер
        _ = asyncio.create_task(dp.start_polling(bot, polling_timeout=30, handle_signals=False))
    else:
        logger.info('Installing webhook...')
        installed = await bot.set_webhook(f'https://{settings.DOMAIN}/{WEBHOOK_PATH}')
        logger.info(f'Webhook: {installed}')


async def on_shutdown():
    if settings.DEBUG:
        await dp.stop_polling()
    else:
        logger.info('Deleting webhook...')
        installed = not await bot.delete_webhook()
        logger.info(f'Webhook: {installed}')
