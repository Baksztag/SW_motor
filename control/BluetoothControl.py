import socket
from control.Command import Command
from control.command_types import *

HOST_MAC_ADDRESS = 'b8:27:eb:16:7a:5c'
PORT = 3
BACKLOG = 1
SIZE = 1024


class BluetoothControl:
    def __init__(self, queue):
        self.__command_queue = queue

    def __push_command(self, command):
        self.__command_queue.put(command)

    def __parse_command(self, command):
        split_command = str(command)[2:-1].split(':')
        if len(split_command) == 2:
            return {
                'x': int(split_command[0]),
                'y': int(split_command[1])
            }
        return {}

    def run(self):
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.bind((HOST_MAC_ADDRESS, PORT))
        s.listen(BACKLOG)

        client, address = s.accept()
        while True:
            data = client.recv(SIZE)
            command = self.__parse_command(data)
            if command['x'] > 0:
                self.__push_command(Command(GO_FORWARD))
            if command['x'] < 0:
                self.__push_command(Command(GO_BACKWARD))
            print(command)
