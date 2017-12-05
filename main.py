import queue

from vehicle.Vehicle import Vehicle
from control.KeyboardControl import KeyboardControl

command_queue = queue.Queue(50)

vehicle = Vehicle(command_queue)
control = KeyboardControl(command_queue)

vehicle.start()
control.run()
vehicle.join()
