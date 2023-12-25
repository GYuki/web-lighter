from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler

from src.domain.models.server.serverrepository import ServerRepository


class UpdateServerCpuCommandRequest(BaseRequest):
    def __init__(self, address, cpu):
        super().__init__()
        self._address = address
        self._cpu = cpu

    @property
    def address(self):
        return self._address

    @property
    def cpu(self):
        return self._cpu


class UpdateServerCpuCommandResponse(BaseResponse):
    def __init__(self, status):
        super().__init__()
        self._status = status

    @property
    def status(self):
        return self._status


class UpdateServerCpuCommandHandler(BaseHandler):
    def __init__(self, repository: ServerRepository):
        super().__init__()
        self._repository = repository

    async def handle(self, req: UpdateServerCpuCommandRequest):
        server = await self._repository.get_server_by_address(req.address)
        server.set_cpu_level(req.cpu)
        result = await self._repository.update_server(server)
        return UpdateServerCpuCommandResponse(
            status=result
        )
