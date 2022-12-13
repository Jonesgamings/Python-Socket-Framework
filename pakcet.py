from time import time
from pickle import dumps, loads

TYPES = {
    "CONNECT": "CONNECT".encode(),
    "DISCONNECT": "DISCONNECT".encode(),
    "AUTHENTICATE": "AUTHENTICATE".encode()
}

def add_type(new_type):
    if new_type not in TYPES.keys():
        TYPES[new_type] = new_type.encode()

class Packet:

    """ A class to hold a message being sent across a network"""

    def __init__(self, sender, auth_code, type_, data) -> None:
        self.sender = sender
        self.auth_code = auth_code
        self.type = type_
        self.data = data

    def serialize(self):

        """ Converts packet into a network sendable form """

        json = {
            "SENDER": self.sender,
            "AUTH_CODE": self.auth_code,
            "TYPE": self.type,
            "DATA": self.data,
            "TIME": time()
        }

        return dumps(json)

    @classmethod
    def unserialize(cls, serialized):

        """ Converts a network message into the packet class """

        json = loads(serialized)
        new_packet = Packet(json["SENDER"], json["AUTH_CODE"], json["TYPE"], json["DATA"])
        delay = time() - json["TIME"]
        return new_packet, delay

    @classmethod
    def send(cls, recipent, sender, auth_code, type_, data):

        """ Send a packet """

        new_packet = Packet(sender, auth_code, type_, data)
        recipent.send(new_packet.serialize())

if __name__ == "__main__":
    pass