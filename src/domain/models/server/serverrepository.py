from abc import ABC, abstractmethod


class ServerRepository(ABC):
    @abstractmethod
    def add_server(self, server):
        pass

    @abstractmethod
    def remove_server(self, ip):
        pass

    @abstractmethod
    def get_all_servers(self):
        pass

    @abstractmethod
    def get_server_by_ip(self, ip):
        pass

    @abstractmethod
    def get_server_by_domain(self, domain):
        pass
