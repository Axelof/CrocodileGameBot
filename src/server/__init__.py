from fastapi import FastAPI

import vk.signals as vk
import telegram.signals as telegram
from scheduler import scheduler

app = FastAPI(
    on_startup=[
        scheduler.start,
        telegram.on_startup,
        vk.on_startup
    ],
    on_shutdown=[
        scheduler.shutdown,
        telegram.on_shutdown,
        vk.on_shutdown

    ]
)