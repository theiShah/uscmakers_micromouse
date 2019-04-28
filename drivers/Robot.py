import drivers.driver_config as driver_config
from drivers.Encoder import Encoder
from drivers.InfraredSensor import InfraredSensor
from drivers.Motor import Motor
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

class Robot:

    def __init__(self):

        GPIO.setmode(GPIO.BCM)

        self.leftEncoder = Encoder(driver_config.leftEncoderA, driver_config.leftEncoderB)
        self.rightEncoder = Encoder(driver_config.rightEncoderA, driver_config.rightEncoderB)

        adc = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(driver_config.SPI_PORT, driver_config.SPI_DEVICE))

        self.frontInfrared = InfraredSensor(driver_config.frontInfraredChannel, adc)
        self.leftInfrared = InfraredSensor(driver_config.leftInfraredChannel, adc)
        self.rightInfrared = InfraredSensor(driver_config.rightInfraredChannel, adc)

        self.leftMotor = Motor(driver_config.leftMotorPin)
        self.rightMotor = Motor(driver_config.rightMotorPin)

    def move_forward(self):
        pass

    def turn_right(self):
        pass

    def turn_left(self):
        pass

    def get_front(self):
        distance = self.frontInfrared.getDistance()
        if distance > driver_config.frontThreshold or distance < driver_config.infraredLowerThreshold:
            return 0
        else:
            return 1

    def get_left(self):
        distance = self.leftInfrared.getDistance()
        if distance > driver_config.leftThreshold or distance < driver_config.infraredLowerThreshold:
            return 0
        else:
            return 1

    def get_right(self):
        distance = self.rightInfrared.getDistance()
        if distance > driver_config.rightThreshold or distance < driver_config.infraredLowerThreshold:
            return 0
        else:
            return 1
