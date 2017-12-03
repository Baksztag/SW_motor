# import time
import threading
from vehicle.VehicleDrive import VehicleDrive
from control.command_types import *


class Vehicle(threading.Thread):
    def __init__(self, queue, lock):
        threading.Thread.__init__(self)
        self.__drive = VehicleDrive()
        self.__command_queue = queue
        self.__queue_lock = lock

    def execute_command(self, command):
        if command == START:
            pass
        elif command == STOP:
            pass
        elif command == GO_FORWARD:
            pass
        elif command == GO_BACKWARD:
            pass
        elif command == GO_LEFT:
            pass
        elif command == GO_RIGHT:
            pass
        else:
            pass

    def run(self):
        self.__drive.start()
        # TODO Implement Command queue
        while True:
            self.__queue_lock.acquire()
            if not self.__command_queue.empty():
                command = self.__command_queue.get()
                self.execute_command(command)
                self.__queue_lock.release()
            else:
                self.__queue_lock.release()
        # time.sleep(1)
        # self.__drive.drive_back()
        # time.sleep(1)
        # self.__drive.drive_back()
        # time.sleep(1)
        # self.__drive.drive_back()
        # time.sleep(1)
        # self.__drive.drive_back()
        # self.__drive.join()
