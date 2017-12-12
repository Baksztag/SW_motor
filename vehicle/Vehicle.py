import threading
from vehicle.VehicleDrive import VehicleDrive
from control.command_types import *


class Vehicle(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.__drive = VehicleDrive()
        self.__command_queue = queue

    def execute_command(self, command):
        if command.type == START:
            self.__drive.start_vehicle()
        elif command.type == STOP:
            self.__drive.stop_vehicle()
        elif command.type == GO_FORWARD:
            self.__drive.go_forward(command.speed, command.ratio)
        elif command.type == GO_BACKWARD:
            self.__drive.go_backwards(command.speed, command.ratio)
        # elif command.type == GO_LEFT:
        #     self.__drive.turn_left(command.value)
        # elif command.type == GO_RIGHT:
        #     self.__drive.turn_right(command.value)
        else:
            pass

    def run(self):
        self.__drive.start()
        while True:
            command = self.__command_queue.get()
            self.execute_command(command)
