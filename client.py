from pakcet import *

class Client:

    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        self.packets_recieved = []

    def pakcets(self):
        return self.packets_recieved.copy()

    def update(self):
        self.packets_recieved = []