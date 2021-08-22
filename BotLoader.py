from bots.RandomAI import *
from bots.AStar import *
from bots.ZStar import *

# Bot loader
# Loads all bots in the 'bots' folder
# Adds the bots as buttons on the menu
# passed in arg
class BotLoader():
	def __init__(self, menu):
		self.menu = menu

	# Loads bots
	def load_bots(self):
		#RandomAI
		randomAI = RandomAI()
		self.menu.add.button(randomAI.name, self.AI_play, randomAI)

		#AStar
		astar = AStar()
		self.menu.add.button(astar.name, self.AI_play, astar)

		#ZStar
		zstar = ZStar()
		self.menu.add.button(zstar.name, self.AI_play, zstar)

		# ADD BOTS HERE


	# Launches a game controlled by the AI passed in param
	def AI_play(self, AI):
		self.menu.disable()
		AI.lives = int(self.menu.lives.get_value())
		self.menu.parent.play(AI)