import json

from src.domain.models.server.server import Server


class RedisServerMapper(object):
    @classmethod
    def map_to_redis(cls, server: Server):
        return json.dumps(
            {
                'ip': server.ip_address,
                'domain': server.domain,
                'cpu': server.cpu_level
            }
        )

    @classmethod
    def map_from_redis(cls, server_string):
        server = json.loads(server_string)
        return Server(
            server['ip'],
            server['domain'],
            server['cpu']
        )
