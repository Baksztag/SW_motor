import threading
from vehicle.VehicleDrive import VehicleDrive


class Vehicle(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__drive = VehicleDrive()

    def run(self):
        self.__drive.start()
        # TODO Implement Command queue
        self.__drive.join()
