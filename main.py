import queue

from vehicle.Vehicle import Vehicle
# from control.KeyboardControl import KeyboardControl
from control.BluetoothControl import BluetoothControl

command_queue = queue.Queue(100)

# vehicle = Vehicle(command_queue)
# control = KeyboardControl(command_queue)
#
# vehicle.start()
# control.run()
# vehicle.join()

vehicle = Vehicle(command_queue)
control = BluetoothControl(command_queue)
vehicle.start()
control.run()
vehicle.join()
