import random, pygame
from Directions import *


# Player : the player of the game
# Can be the user or an AI
# AI must implement this class
# The game asks for the direction the snake
# has to take every time he is moving through
# the function 'decision(self)'
class Player():
	def __init__(self):
		self.bestScore = 0
		self.lives = 0
		self.name = ""
	
	def decision(self, grid, snake, apple):
		pass

# User : the user plays the game
# The snake is controlled with
# the arrows on the keyboard 
class User(Player):
	def __init__(self):
		Player.__init__(self)
		self.buffer = random.choice(list(Directions)).value

	def decision(self, grid, snake, apple):
		self.handle_keys()
		return self.buffer

	# Handles the keys that the 
	# user presses
	def handle_keys(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.buffer = Directions.UP.value
				elif event.key == pygame.K_DOWN:
					self.buffer = Directions.DOWN.value
				elif event.key == pygame.K_LEFT:
					self.buffer = Directions.LEFT.value
				elif event.key == pygame.K_RIGHT:
					self.buffer = Directions.RIGHT.value