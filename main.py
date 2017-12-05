import queue
import threading

from vehicle.Vehicle import Vehicle
from control.KeyboardControl import KeyboardControl

command_queue = queue.Queue(50)
queue_lock = threading.Lock()

vehicle = Vehicle(command_queue, queue_lock)
control = KeyboardControl(command_queue, queue_lock)

vehicle.start()
control.run()
vehicle.join()
