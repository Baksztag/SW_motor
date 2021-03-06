import time
import threading
import RPi.GPIO as GPIO


class Motor(threading.Thread):
    def __init__(self, threadID, name, pins, motor_control):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.__control = motor_control
        self.__sequence = [
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1]
        ]
        self.__pins = pins
        self.__max_speed = 1000.0
        self.__set_up_pins()

    def __set_up_pins(self):
        GPIO.setmode(GPIO.BCM)
        for pin in self.__pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

    def run(self):
        step_count = len(self.__sequence)
        step_counter = 0

        while True:
            while self.__control.speed > 0.000001 and self.__control.running:
                for pin in range(0, 4):
                    xpin = self.__pins[pin]
                    if self.__sequence[step_counter][pin] != 0:
                        GPIO.output(xpin, True)
                    else:
                        GPIO.output(xpin, False)

                step_counter += self.__control.direction
                if step_counter >= step_count:
                    step_counter = 0
                if step_counter < 0:
                    step_counter = step_count - 1

                time.sleep(1 / (self.__max_speed * self.__control.speed))
