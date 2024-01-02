from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton, Factory
from redis.asyncio import ConnectionPool

from src.api.queries.roomqueries import RoomQueries
from src.api.queries.serverqueries import ServerQueries
from src.infrastructure.repositories.redisroomrepository import RedisRoomRepository
from src.infrastructure.repositories.redisserverrepository import RedisServerRepository


class Container(DeclarativeContainer):
    _redis = Singleton(
        ConnectionPool.from_url,
        url='redis://192.168.30.128'
    )

    room_repository = Factory(
        RedisRoomRepository,
        pool=_redis
    )

    server_repository = Factory(
        RedisServerRepository,
        pool=_redis
    )

    # queries
    room_queries = Factory(
        RoomQueries,
        repository=room_repository
    )

    server_queries = Factory(
        ServerQueries,
        repository=server_repository
    )
