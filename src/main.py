import asyncio
import os

import uvicorn
from fastapi import FastAPI

from src.api.eventbus.eventshandler import on_server_cpu_update, on_room_create, on_server_create, on_room_delete, \
    on_server_remove, on_room_players_update
from src.api.eventbus.consumer import AsyncioRabbitMQ
from src.container import Container
from src.mediator_setup import set_up
from src.api.controllers import roomcontroller as room_api
from src.api.controllers import servercontroller as server_api
from src.api.commands import createservercommand as csc
from src.api.commands import createroomcommand as crc
from src.api.commands import updateplayerscommand as upc
from src.api.notifications import roomcreatednotification as rcn
from src.api.commands import deleteroomcommand as drc


container = Container()
container.wire(modules=[room_api, server_api, csc, crc, upc, rcn, drc])

set_up()

app = FastAPI()
app.include_router(room_api.router)
app.include_router(server_api.router)


@app.on_event("startup")
async def startup() -> None:
    user = os.environ['RABBITMQ_DEFAULT_USER']
    passwd = os.environ['RABBITMQ_DEFAULT_PASS']
    host = os.environ['RABBITMQ_HOST']
    port = os.environ['RABBITMQ_PORT']

    ep = AsyncioRabbitMQ(f'amqp://{user}:{passwd}@{host}:{port}/%2F')
    ep.connect()
    await asyncio.sleep(1)  # Wait for MQ
    ep.read_messages("server_cpu_update", on_server_cpu_update)
    ep.read_messages("room_create", on_room_create)
    ep.read_messages("server_create", on_server_create)
    ep.read_messages("room_delete", on_room_delete)
    ep.read_messages("server_remove", on_server_remove)
    ep.read_messages("room_players_update", on_room_players_update)


uvicorn.run(app, host="127.0.0.1", port=80)
