import uvicorn
from fastapi import FastAPI

from src.api.controllers.loadbalancer import router
from src.container import Container
from src.mediator_setup import set_up
from src.api.controllers import loadbalancer as lb_api


container = Container()
container.wire(modules=[lb_api])

set_up()

app = FastAPI()
app.include_router(router)
uvicorn.run(app, host="127.0.0.1", port=8000)
