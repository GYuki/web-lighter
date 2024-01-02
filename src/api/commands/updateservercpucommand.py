from dependency_injector.wiring import Provide
from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler

from src.container import Container
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
    def __init__(self):
        super().__init__()

    async def handle(self, req: UpdateServerCpuCommandRequest, server_repository: ServerRepository = Provide[Container.server_repository]):
        server = await server_repository.get_server_by_address(req.address)
        server.set_cpu_level(req.cpu)
        result = await server_repository.update_server(server)
        return UpdateServerCpuCommandResponse(
            status=result
        )
