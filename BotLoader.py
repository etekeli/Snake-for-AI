from bots.RandomAI import *
from bots.AStar import *

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

		#RandomAI
		astar = AStar()
		self.menu.add.button(astar.name, self.AI_play, astar)

		# ADD BOTS HERE


	# Launches a game controlled by the AI passed in param
	def AI_play(self, AI):
		self.menu.disable()
		AI.lives = int(self.menu.lives.get_value())
		self.menu.parent.play(AI)