from control.Command import Command
from control.command_types import *


class KeyboardControl:
    def __init__(self, queue):
        self.__command_queue = queue

    def __push_command(self, command):
        self.__command_queue.put(command)

    def run(self):
        while True:
            char = input('>>> ')
            if char == 'w':
                self.__push_command(Command(GO_FORWARD))
            elif char == 's':
                self.__push_command(Command(GO_BACKWARD))
            elif char == 'a':
                self.__push_command(Command(GO_LEFT))
            elif char == 'd':
                self.__push_command(Command(GO_RIGHT))
            elif char == 'x':
                self.__push_command(Command(STOP))
            elif char == 'z':
                self.__push_command(Command(START))
            else:
                pass
