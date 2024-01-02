from dependency_injector.wiring import Provide, inject

from src.container import Container
from src.domain.models.server.serverrepository import ServerRepository


class ServerQueries(object):
    @inject
    def __init__(self, repository: ServerRepository = Provide[Container.server_repository]):
        self._repository = repository

    def get_best_server(self):
        return self._repository.get_best_server()
