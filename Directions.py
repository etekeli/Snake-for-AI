from enum import Enum

# Directions: Directions tha can take the snake
# The snake can go left, top, right or down
class Directions(Enum):
	LEFT = (-1,0)
	UP = (0, -1)
	RIGHT = (1, 0)
	DOWN = (0, 1)