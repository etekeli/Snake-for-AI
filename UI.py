import pygame, pygame_menu
from Player import *
from BotLoader import BotLoader
from config import *

MENU_SCALE = 1

# Main Menu : displays the main menu
# The button 'Play' launches a game controlled by the user
# The button AI displays the AI Menu
# The button Quit exits the game
class MainMenu(pygame_menu.Menu):
	def __init__(self, parent):
		self.parent = parent 
		pygame_menu.Menu.__init__(self,
				width = MENU_SCALE * WINDOW_WIDTH, 
				height = MENU_SCALE * WINDOW_HEIGHT,
				theme=pygame_menu.themes.THEME_GREEN,
				title = "Main menu")

		# User plays the game
		self.add.button('Play', self.user_play)

		# Number of retry
		self.lives = self.add.text_input('Lives: ', default='10', input_type=pygame_menu.locals.INPUT_INT)

		# AI Menu
		aimenu = AIMenu(parent)
		# Need to explicitely tell pygame-menu that this is a pygame_menu.Menu to prevent crash
		self.__class__ = pygame_menu.Menu 
		self.add.button('AI', aimenu)

		# Exit game
		self.add.button('Quit', pygame_menu.events.EXIT)

	# Launches a game controlled by the user
	def user_play(self):
		self.disable()
		player = User()
		player.lives = int(self.lives.get_value())
		self.parent.play(player)

# AI Menu : displays the AI list
# Chose an AI that will play the game
class AIMenu(pygame_menu.Menu):
	def __init__(self, parent):
		self.parent = parent
		pygame_menu.Menu.__init__(self,
				width= MENU_SCALE * WINDOW_WIDTH,
				height= MENU_SCALE * WINDOW_HEIGHT,
				theme = pygame_menu.themes.THEME_GREEN,
				title= 'Chose AI')

		# Number of retry
		self.lives = self.add.text_input('Lives: ', default='10', input_type=pygame_menu.locals.INPUT_INT)

		# Load bots
		bl = BotLoader(self)
		bl.load_bots()

		# Back to main menu
		self.add.button('Return to main menu', pygame_menu.events.RESET)

	# Launches a game controlled by the AI passed in param
	def AI_play(self, AI):
		self.disable()
		AI.lives = int(self.lives.get_value())
		self.parent.play(AI)

# HUD
# Prints the player's name,
# the game score,
# number of lives left
# and the player's best score
class HUD():
	def __init__(self, screen):
		self.screen = screen
		self.font = pygame.font.SysFont("calibri", 20)

	def draw(self, score, player):
		text = self.font.render("Player: " + player.name + "   Best Score: " + str(player.bestScore), 1, (0,0,0))
		self.screen.blit(text, (5,10))
		text = self.font.render("Score: " + str(score) + "   Lives: " + str(player.lives), 1, (0,0,0))
		self.screen.blit(text, (5,50))
		text = self.font.render("+ => x2 ", 1, (31,231,31))
		self.screen.blit(text, (WINDOW_WIDTH - 90,10))
		text = self.font.render("- => /2 ", 1, (231,31,31))
		self.screen.blit(text, (WINDOW_WIDTH - 90,50))

