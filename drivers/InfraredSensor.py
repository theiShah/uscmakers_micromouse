
import driver_config

class InfraredSensor():

	def __init__(self, channel, adc):
		self.adc = adc
		self.channel = channel

	def getDistance(self):

		raw_value = self.adc.read_adc(self.channel)

		return raw_value * driver_config.infraredConversionFactor