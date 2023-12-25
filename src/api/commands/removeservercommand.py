from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler

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
    def __init__(self, repository: ServerRepository):
        super().__init__()
        self._repository = repository

    async def handle(self, req: RemoveServerCommandRequest):
        result = await self._repository.remove_server(req.address)
        return RemoveServerCommandResponse(
            status=result
        )
