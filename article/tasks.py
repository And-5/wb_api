import asyncio
from wb_api.celery import app

from .services import choose_interval, get_list_file


@app.task
def get_data(art):
    asyncio.run(choose_interval(art))


@app.task
def get_file():
    asyncio.run(get_list_file())
