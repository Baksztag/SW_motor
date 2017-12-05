import socket

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
        split_command = command.split(';')
        if len(split_command) == 2:
            return {
                'x': split_command[0],
                'y': split_command[1]
            }
        return {}

    def run(self):
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.bind((HOST_MAC_ADDRESS, PORT))
        s.listen(BACKLOG)

        try:
            client, address = s.accept()
            while True:
                data = client.recv(SIZE)
                command = self.__parse_command(data)
                print(command)
        except:
            print("Closing socket")
            client.close()
            s.close()
