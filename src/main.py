import uvicorn
from fastapi import FastAPI
from src.container import Container
from src.mediator_setup import set_up
from src.api.controllers import roomcontroller as room_api
from src.api.controllers import servercontroller as server_api


container = Container()
container.wire(modules=[room_api, server_api])

set_up()

app = FastAPI()
app.include_router(room_api.router)
app.include_router(server_api.router)
uvicorn.run(app, host="127.0.0.1", port=8000)
