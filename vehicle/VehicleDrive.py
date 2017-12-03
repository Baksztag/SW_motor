import threading
from motor.Motor import Motor
from motor.MotorControl import MotorControl

LEFT_MOTOR_NAME = 'LEFT_MOTOR'
RIGHT_MOTOR_NAME = 'RIGHT_MOTOR'
LEFT_MOTOR_PINS = []
RIGHT_MOTOR_PINS = []


class VehicleDrive(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__left_motor_control = MotorControl(direction=-1)
        self.__right_motor_control = MotorControl()
        self.__left_motor = Motor(1, LEFT_MOTOR_NAME, LEFT_MOTOR_PINS, self.__left_motor_control)
        self.__right_motor = Motor(2, RIGHT_MOTOR_NAME, RIGHT_MOTOR_PINS, self.__right_motor_control)

    def run(self):
        self.__left_motor.start()
        self.__right_motor.start()

        self.__left_motor_control.run_motor()
        self.__right_motor_control.run_motor()

        self.__left_motor.join()
        self.__right_motor.join()

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def drive_back(self):
        self.__left_motor_control.switch_direction()
        self.__right_motor_control.switch_direction()