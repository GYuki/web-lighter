from src.domain.models.server.serverrepository import ServerRepository


class ServerQueries(object):
    def __init__(self, repository: ServerRepository):
        self._repository = repository

    def get_best_server(self):
        return self._repository.get_best_server()
