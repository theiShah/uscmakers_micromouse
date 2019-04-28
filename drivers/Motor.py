
class Motor():

	def __init__(self, channelA, channelB):
		self.channelA = channelA
		self.channelB = channelB

	def setSpeed(self, speed):
		
		if speed == 0:
			pass
		else:
			direction = speed/abs(speed)
