# Set up the encoders without classes

import RPi.GPIO as GPIO

# encoderRPins = [18, 25]
# encoderLPins = [4, 17]

class Encoder():

    def __init__(self, channelA, channelB):

        self.channelA = channelA
        self.channelB = channelB

        GPIO.setup(self.channelA, GPIO.IN)
        GPIO.setup(self.channelB, GPIO.IN)
        GPIO.add_event_detect(self.channelA, GPIO.BOTH, callback=lambda x: self.UpdateCount(x))
        GPIO.add_event_detect(self.channelB, GPIO.BOTH, callback=lambda x: self.UpdateCount(x))

        self.encoderCount = 0
        self.encoderState = 0

    def UpdateCount(self, channel):
        a = GPIO.input(self.channelA)
        b = GPIO.input(self.channelB)

        if self.encoderState == 0:
            if not b and a:
                self.encoderState = 1
                self.encoderCount += 1
            elif b and not a:
                self.encoderState = 2
                self.encoderCount -= 1
        elif self.encoderState == 1:
            if not b and not a:
                self.encoderState = 0
                self.encoderCount -= 1
            elif b and a:
                self.encoderState = 3
                self.encoderCount += 1
        elif self.encoderState == 2:
            if b and a:
                self.encoderState = 3
                self.encoderCount -= 1
            elif not b and not b:
                self.encoderState = 0
                self.encoderCount += 1
        elif self.encoderState == 3:
            if b and not a:
                self.encoderState = 2
                self.encoderCount += 1
            elif not b and a:
                self.encoderState = 1
                self.encoderCount -= 1

    def getCount(self):
        return self.encoderCount