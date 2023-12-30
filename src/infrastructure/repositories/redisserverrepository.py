from redis.asyncio import Redis, ConnectionPool

from src.domain.models.server.serverrepository import ServerRepository
from src.infrastructure.mappers.redis.server import RedisServerMapper


class RedisServerRepository(ServerRepository):
    def __init__(self, pool: ConnectionPool):
        self._connection = Redis.from_pool(pool)

    async def add_server(self, server):
        await self._connection.hset("servers", RedisServerMapper.map_to_redis(server))
        return True

    async def update_server(self, server):
        await self._update_server_load(server)
        result = await self.add_server(server)
        return result

    async def _update_server_load(self, server):
        await self._connection.zadd("server_load", server.address, server.cpu_level)

    async def _get_best_loaded_server(self):
        result = await self._connection.zrange("server_load", 0, 1)
        return result

    async def remove_server(self, address):
        await self._connection.hdel("servers", address)
        return True

    async def get_all_servers(self):
        servers = [RedisServerMapper.map_to_redis(s) for s in await self._connection.hvals("servers")]
        return servers

    async def get_server_by_address(self, address):
        server = await self._connection.hget("servers", address)
        return RedisServerMapper.map_from_redis(server)

    async def get_best_server(self):
        result = None
        _server_key = await self._get_best_loaded_server()
        if _server_key:
            result = await self.get_server_by_address(_server_key)
        return result
