


class State:

	def __init__(self,id):
		self.id = id
		self.value = 0
		if id == 9:
			self.terminal = False
		else:
			self.terminal = True

	def updateValue(self,value):
		self.value = value
 
