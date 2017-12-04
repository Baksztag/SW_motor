from control.Command import Command
from control.command_types import *


class KeyboardControl:
    def __init__(self, queue, lock):
        self.__command_queue = queue
        self.__queue_lock = lock

    def __push_command(self, command):
        self.__queue_lock.acquire()
        self.__command_queue.push(command)
        self.__queue_lock.release()

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
