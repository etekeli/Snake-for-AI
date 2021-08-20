import random, pygame
from UI import WINDOW_HEIGHT, WINDOW_WIDTH
from Directions import *


# Grid : Grid on which the snake moves
class Grid():
	def __init__(self):
		self.size = 20
		self.cell_width = WINDOW_WIDTH / self.size
		self.cell_height = WINDOW_HEIGHT / self.size
		self.color1 = (170, 170, 170)
		self.color2 = (223, 224, 226)
		
	# Draws the grid with a checker style
	def draw(self, surface):
		for y in range(0, self.size):
			for x in range(0, int(self.size)):
				if (x+y)%2 == 0:
					r = pygame.Rect((x*self.cell_width, y*self.cell_height), (self.cell_width,self.cell_height))
					pygame.draw.rect(surface, self.color1, r)
				else:
					rr = pygame.Rect((x*self.cell_width, y*self.cell_height), (self.cell_width,self.cell_height))
					pygame.draw.rect(surface, self.color2, rr)


# Snake : Snake that is controlled by a player
class Snake():
	def __init__(self, grid):
		self.grid = grid
		self.color = (7, 16, 19)
		self.color2= (206, 245, 66)
		self.reset()

	# Resets the snake
	def reset(self):
		# Start with a random direction
		self.direction = random.choice(list(Directions)).value

		# Snake's length
		self.length = 1

		# The body of the snake is a list of positions
		# The first element of that list is the head
		head = (0, 0)
		self.body = [head]
		self.randomize_position()

	# Returns the head of the snake
	def head(self):
		return self.body[0]

	# Makes the snake turn
	# the snake can't make an instant U turn
	# if his length is greater than 1
	def turn(self, direction):
		if self.length == 1 or (direction[0]*-1, direction[1]*-1) != self.direction:
			self.direction = direction

	# Moves the snake
	# Returns 0 if game over, 1 if not
	def move(self):
		x,y = self.direction[0], self.direction[1]
		new_pos = (((self.head()[0]+x) %self.grid.size), ((self.head()[1]+y) %self.grid.size))
		if self.collisionHappens(new_pos):
			self.reset() # GAME OVER
			return 0
		else:
			self.body.insert(0, new_pos)
			if len(self.body) > self.length:
				self.body.pop()
			return 1

	# Checks if a collision happens
	def collisionHappens(self, position):
		return (len(self.body) > 2 and position in self.body[2:])


	# Randomize the position of the snake's head
	def randomize_position(self):
		self.body[0] = (random.randint(0, self.grid.size-1), random.randint(0, self.grid.size-1))

	# Draws the snake
	def draw(self,surface):
		for square in self.body:
			r = pygame.Rect((square[0]*self.grid.cell_width, square[1]*self.grid.cell_height), (self.grid.cell_width,self.grid.cell_height))
			pygame.draw.rect(surface, self.color, r)
			pygame.draw.rect(surface, self.color2, r, 2)


# Apple : is eaten by the snake
# Increases the score and makes
# the snake grow
class Apple():
	def __init__(self, grid, snake):
		self.grid = grid
		self.bonus = 10
		self.position = (0,0)
		self.randomize_position(snake)
		self.color = (235, 81, 96)
		self.color2 = (250, 32, 54)

	# Draws the apple
	def draw(self, surface):
		r = pygame.Rect((self.position[0]*self.grid.cell_width, self.position[1]*self.grid.cell_height), (self.grid.cell_width, self.grid.cell_height))
		pygame.draw.rect(surface, self.color, r)
		pygame.draw.rect(surface, self.color2, r, 9)

	def randomize_position(self, snake):
		self.position = (random.randint(0, self.grid.size-1), random.randint(0, self.grid.size-1))