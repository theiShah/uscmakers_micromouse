
import RPi.GPIO as GPIO

class Motor():

    def __init__(self, channelA, channelB, pi):
        self.channelA = channelA
        self.channelB = channelB
        self.pi = pi
        GPIO.setup(self.channelA, GPIO.OUT)
        GPIO.setup(self.channelB, GPIO.OUT)
        self.pi.set_PWM_frequency(self.channelA, 1000)
        self.pi.set_PWM_dutycycle(self.channelA, 0)
        self.pi.set_PWM_frequency(self.channelB, 1000)
        self.pi.set_PWM_dutycycle(self.channelB, 0)
        

    def setSpeed(self, speed):
        
        speed = max(min(speed, 1.0), -1.0)

        if speed == 0:
            direction = 1
        else:
            direction = speed/abs(speed)
        
        if direction > 0 :
            self.pi.set_PWM_dutycycle(self.channelA, speed * 255)
            self.pi.set_PWM_dutycycle(self.channelB, 0)
        else:
            self.pi.set_PWM_dutycycle(self.channelA, 0)
            self.pi.set_PWM_dutycycle(self.channelB, direction * speed * 255)
