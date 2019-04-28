
class InfraredSensor():

	def __init__(self, channel, adc):
		self.adc = adc
		self.channel = channel

	def getDistance(self):
		return -1
