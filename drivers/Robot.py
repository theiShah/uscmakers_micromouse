import drivers.driver_config as driver_config
from drivers.Encoder import Encoder
from drivers.InfraredSensor import InfraredSensor
from drivers.Motor import Motor
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import pigpio
import time

pigpio = pigpio.pi()

class Robot:

    def __init__(self):

        GPIO.setmode(GPIO.BCM)

        #self.leftEncoder = Encoder(driver_config.leftEncoderA, driver_config.leftEncoderB)
        #self.rightEncoder = Encoder(driver_config.rightEncoderA, driver_config.rightEncoderB)

        adc = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(driver_config.SPI_PORT, driver_config.SPI_DEVICE))
        #pigpio = pigpio.pi()


        self.frontInfrared = InfraredSensor(driver_config.frontInfraredChannel, adc)
        self.leftInfrared = InfraredSensor(driver_config.leftInfraredChannel, adc)
        self.rightInfrared = InfraredSensor(driver_config.rightInfraredChannel, adc)

        self.leftMotor = Motor(driver_config.leftMotorPinA, driver_config.leftMotorPinB, pigpio)
        self.rightMotor = Motor(driver_config.rightMotorPinA, driver_config.rightMotorPinB, pigpio)
        
        while True:
            self.move_forward()
            self.turn_right()
            time.sleep(0.5)
            self.move_forward()
            self.turn_right()
            time.sleep(0.5)
            self.move_forward()
            self.turn_right()
            time.sleep(0.5)
            self.move_forward()
            self.turn_right()
            time.sleep(1.0)
            #self.turn_left()
            time.sleep(2.5)

        while True:
            print("{} {} {}".format(self.frontInfrared.getDistance(), self.leftInfrared.getDistance(), self.rightInfrared.getDistance()))
            time.sleep(0.1)

    def move_forward(self):
        # This should be re-written to use PID
        self.leftMotor.setSpeed(0.5)
        self.rightMotor.setSpeed(0.5)
        #time.sleep(0.68)
        for i in range (0, 7):
            if self.get_short_front():
                break
            time.sleep(0.1)
        self.leftMotor.setSpeed(0)
        self.rightMotor.setSpeed(0)

    def turn_right(self):
        # This should be re-written to use PID
        self.leftMotor.setSpeed(0.5)
        self.rightMotor.setSpeed(-0.5)
        time.sleep(0.25)
        self.leftMotor.setSpeed(0)
        self.rightMotor.setSpeed(0)

    def turn_left(self):
        # This should be re-written to use PID
        self.leftMotor.setSpeed(-0.5)
        self.rightMotor.setSpeed(0.5)
        time.sleep(0.25)
        self.leftMotor.setSpeed(0)
        self.rightMotor.setSpeed(0)

    def get_front(self):
        distance = self.frontInfrared.getDistance()
        if distance > driver_config.frontThreshold:
            return 0
        else:
            return 1

    def get_short_front(self):
        distance = self.frontInfrared.getDistance()
        if distance > driver_config.frontShortThreshold:
            return 0
        else:
            return 1

    def get_left(self):
        distance = self.leftInfrared.getDistance()
        if distance > driver_config.leftThreshold:
            return 0
        else:
            return 1

    def get_right(self):
        distance = self.rightInfrared.getDistance()
        if distance > driver_config.rightThreshold:
            return 0
        else:
            return 1
