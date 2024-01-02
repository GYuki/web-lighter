from dependency_injector.wiring import Provide, inject
from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler

from src.container import Container
from src.domain.models.server.serverrepository import ServerRepository


class RemoveServerCommandRequest(BaseRequest):
    def __init__(self, address):
        super().__init__()
        self._address = address

    @property
    def address(self):
        return self._address
    

class RemoveServerCommandResponse(BaseResponse):
    def __init__(self, status):
        super().__init__()
        self._status = status

    @property
    def status(self):
        return self._status


class RemoveServerCommandHandler(BaseHandler):
    def __init__(self):
        super().__init__()

    @inject
    async def handle(self, req: RemoveServerCommandRequest, server_repository: ServerRepository = Provide[Container.server_repository]):
        result = await server_repository.remove_server(req.address)
        return RemoveServerCommandResponse(
            status=result
        )
