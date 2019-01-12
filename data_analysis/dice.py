from random import randint
class Dice():
	def __init__(self, num_sides=6):
		self.num_sides = num_sides
	def roll(self):
		result = randint(1,self.num_sides)
		return result
