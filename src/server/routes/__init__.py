from typing import Union

from fastapi import FastAPI

from scheduler import scheduler

app = FastAPI(
    on_startup=[
        scheduler.start,
    ],
    on_shutdown=[
        scheduler.shutdown,
    ]
)