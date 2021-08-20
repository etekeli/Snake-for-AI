from Player import *

# Random AI : AI that moves randomly
class RandomAI(Player):
	def __init__(self):
		Player.__init__(self)
		self.name = "RandomAI"
	
	def decision(self, grid, snake, apple):
		return random.choice(list(Directions)).value
