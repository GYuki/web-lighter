from redis import Redis

from src.domain.models.server.serverrepository import ServerRepository
from src.infrastructure.mappers.redis.server import RedisServerMapper


class RedisServerRepository(ServerRepository):
    def __init__(self, connection: Redis):
        self._connection = connection

    def add_server(self, server):
        self._connection.hset("servers", RedisServerMapper.map_to_redis(server))
        return True

    def update_server(self, server):
        self._update_server_load(server)
        return self.add_server(server)

    def _update_server_load(self, server):
        self._connection.zadd("server_load", server.address, server.cpu_level)

    def _get_best_loaded_server(self):
        return self._connection.zrange("server_load", 0, 1)

    def remove_server(self, address):
        self._connection.hdel("servers", address)
        return True

    def get_all_servers(self):
        return [RedisServerMapper.map_to_redis(s) for s in self._connection.hvals("servers")]

    def get_server_by_address(self, address):
        return RedisServerMapper.map_from_redis(self._connection.hget("servers", address))

    def get_best_server(self):
        _server_key = self._get_best_loaded_server()
        if _server_key:
            return self.get_server_by_address(_server_key)
        return None
