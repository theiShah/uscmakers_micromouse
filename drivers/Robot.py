import drivers.driver_config as driver_config
from drivers.Encoder import Encoder

class Robot:

    def __init__(self):
        self.leftEncoder = Encoder(driver_config.leftEncoderA, driver_config.leftEncoderB)
        self.rightEncoder = Encoder(driver_config.rightEncoderA, driver_config.rightEncoderB)

    def move_forward(self):
        pass

    def turn_right(self):
        pass

    def turn_left(self):
        pass

    def get_front(self):
        pass

    def get_left(self):
        pass

    def get_right(self):
        pass
