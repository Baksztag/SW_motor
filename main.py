import queue

# from vehicle.Vehicle import Vehicle
# from control.KeyboardControl import KeyboardControl
from control.BluetoothControl import BluetoothControl

command_queue = queue.Queue(50)

# vehicle = Vehicle(command_queue)
# control = KeyboardControl(command_queue)
#
# vehicle.start()
# control.run()
# vehicle.join()

control = BluetoothControl(command_queue)
control.run()
