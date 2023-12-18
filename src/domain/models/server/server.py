class Server(object):
    def __init__(self, address, domain="", cpu=0):
        self._ip, self._port = self._split_address(address)
        self._domain = domain
        self._cpu = cpu

    def _split_address(self, address):
        return address.split(":")

    @property
    def domain(self):
        return self._domain

    @property
    def ip_address(self):
        return f'{self._ip}:{self._port}'

    @property
    def address(self):
        return self._domain if self._domain else self.ip_address

    @property
    def ws_address(self):
        return 'wss://' if self._domain else 'ws://' + self.address

    def set_cpu_level(self, value):
        self._cpu = value

    @property
    def cpu_level(self):
        return self._cpu
