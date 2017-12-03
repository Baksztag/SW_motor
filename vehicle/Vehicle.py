import time
import threading
from vehicle.VehicleDrive import VehicleDrive


class Vehicle(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__drive = VehicleDrive()

    def run(self):
        self.__drive.start()
        # TODO Implement Command queue
        time.sleep(1)
        self.__drive.drive_back()
        time.sleep(1)
        self.__drive.drive_back()
        time.sleep(1)
        self.__drive.drive_back()
        time.sleep(1)
        self.__drive.drive_back()
        self.__drive.join()
