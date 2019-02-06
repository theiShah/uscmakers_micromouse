
class Stack():

	def __init__(self):
		self.list = []

	def add(self, val):
		self.list.append(val)

	def pop(self):
		return self.list.pop()

	def peek(self):
		return self.list[-1]