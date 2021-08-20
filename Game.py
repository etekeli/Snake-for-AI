import pygame, sys
from UI import *
from Player import *
from GameElements import *

clock = pygame.time.Clock()
FPS = 10

# App : Main class
# Creates the main menu 
# Launches games when asked
# through the function 'play(self, player)'
class App():
	def __init__(self):
		# Init
		pygame.init()
		self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
		self.surface = pygame.Surface(self.screen.get_size())
		self.surface = self.surface.convert()
		pygame.display.set_caption("Snake for AI")

		# Main Menu
		self.main_menu = MainMenu(self)

		# Application loop
		self.app_loop()

	
	# Application loop
	def app_loop(self):
		
		while (True):
			clock.tick(FPS)
			self.check_events()

			pygame.display.update()
	
	# Launches a game
	def play(self, player):
		game = Game(self.screen, self.surface)
		game.game_loop(player)
		self.main_menu.enable()

	# Checks events
	def check_events(self):
		events = pygame.event.get()

		if self.main_menu.is_enabled():
				self.main_menu.update(events)
				self.main_menu.draw(self.screen)

		for event in events:
			if event.type == pygame.QUIT:
				exit()


		
# Game : Snake game
class Game():
	def __init__(self, screen, surface):
		self.screen = screen
		self.surface = surface
		self.grid = Grid()
		self.snake = Snake(self.grid)
		self.apple = Apple(self.grid)
		self.hud = HUD(self.screen)
		self.score = 0

	# Game loop
	def game_loop(self, player):
		while (player.lives):
			clock.tick(FPS)
			self.check_events()	
			self.snake.turn(player.decision(self.grid, self.snake, self.apple))
			self.grid.draw(self.surface)
			if not self.snake.move():
				self.game_over(player)
			self.check_apple(player)
			self.snake.draw(self.surface)
			self.apple.draw(self.surface)
			self.screen.blit(self.surface, (0,0))
			self.hud.draw(self.score, player)
			pygame.display.update()
	
	# Handles game over
	def game_over(self, player):
		if self.score > player.bestScore:
			player.bestScore = self.score
		self.score = 0
		player.lives -= 1

	# Checks if the apple is eaten
	def check_apple(self, player):
		if self.snake.head() == self.apple.position:
				self.snake.length += 1
				self.score += self.apple.bonus
				self.apple.randomize_position()

	# Checks events
	def check_events(self):
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				exit()

if __name__ == '__main__':
	app = App()

	


