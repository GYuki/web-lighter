from redis import Redis

from src.domain.models.server.serverrepository import ServerRepository
from src.infrastructure.mappers.redis.server import RedisServerMapper


class RedisServerRepository(ServerRepository):
    def __init__(self, connection: Redis):
        self._connection = connection

    def add_server(self, server):
        self._connection.hset("servers", RedisServerMapper.map_to_redis(server))
        return True

    def remove_server(self, address):
        self._connection.hdel("servers", address)
        return True

    def get_all_servers(self):
        return [RedisServerMapper.map_to_redis(s) for s in self._connection.hvals("servers")]

    def get_server_by_address(self, address):
        return RedisServerMapper.map_from_redis(self._connection.hget("servers", address))
