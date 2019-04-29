
class Motor():

	def __init__(self, channelA, channelB):
		self.channelA = channelA
		self.channelB = channelB

	def setSpeed(self, speed):
		
		speed = max(min(speed, 1.0), -1.0)

		if speed == 0:
			pass
		else:
			direction = speed/abs(speed)
