from dependency_injector.wiring import Provide
from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler

from src.container import Container
from src.domain.models.server.server import Server
from src.domain.models.server.serverrepository import ServerRepository


class CreateServerCommandRequest(BaseRequest):
    def __init__(self, address, domain):
        super().__init__()
        self._address = address
        self._domain = domain

    @property
    def address(self):
        return self._address

    @property
    def domain(self):
        return self._domain


class CreateServerCommandResponse(BaseResponse):
    def __init__(self, status):
        super().__init__()
        self._status = status

    @property
    def status(self):
        return self._status


class CreateServerCommandHandler(BaseHandler):
    def __init__(self):
        super().__init__()

    async def handle(self, req: CreateServerCommandRequest, server_repository: ServerRepository = Provide[Container.server_repository]):
        server = Server(
            address=req.address,
            domain=req.domain
        )
        result = await server_repository.add_server(server)
        return CreateServerCommandResponse(
            status=result
        )
