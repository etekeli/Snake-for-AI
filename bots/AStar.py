from Player import *
import math, sys
from Utility import *

# AStar : AI that uses the A* algorithm
class AStar(Player):
	def __init__(self):
		Player.__init__(self)
		self.name = "AStar"
	
	def decision(self, grid, snake, apple):
		# The snake's body parts are the obstacles
		maze = [[0 for col in range(grid.size)] for row in range(grid.size)]
		for item in snake.body:
			maze[item[0]][item[1]] = 1
		
		# Starting position
		head = snake.head()

		# Find a path
		path = self.a_star(maze, head, apple.position)

		# To get the direction, we look at the difference between the beginning of the path and the snake's head
		if path:
			first_step = path[1]
			direction = (first_step[0]-head[0], first_step[1]-head[1])
			return direction
		else:
			return snake.direction # No path found

	# Main A* algorithm
	# The maze is a list of list
	# 0 represents a reachable area
	# 1 represents an obstacle
	def a_star(self, maze, start, end):
		# Init lists and nodes
		open = [] # Nodes not treated yet
		closed = [] # Treated nodes
		start_node = AStarNode(None, start) # Start node
		start_node.g = 0
		end_node = AStarNode(None, end) # End node, the target
		open.append(start_node)

		while len(open) > 0:
				# Find the node with the lowest f cost
				current = open[0]
				current_index = 0
				for index, item in enumerate(open):
						if item.f < current.f:
								current = item
								current_index = index

				# Remove current from open and add it to closed
				open.pop(current_index)
				closed.append(current)

				# If the current node is the target, we're done
				if current == end_node:
						return current.path()

				# Discover neighbours of current
				self.discover_neighbours(maze, current, open, closed, end_node)


	# Discovers and manages neighbours of current 
	def discover_neighbours(self, maze, current, open, closed, end_node):
		# Neighbours
		for direction in [d.value for d in Directions]:
				neighbour = AStarNode(current, (current.position[0] + direction[0], current.position[1] + direction[1]))

				# Continue to the next neighbour if neighbour is in closed or is not reachable
				if (neighbour in closed 
					or neighbour.position[0] > (len(maze) - 1) 
					or neighbour.position[0] < 0 
					or neighbour.position[1] > (len(maze[0]) -1) 
					or neighbour.position[1] < 0
					or maze[neighbour.position[0]][neighbour.position[1]]):
						continue

				# If the path is shorter
				if current.g+1 < neighbour.g:
					# Set costs
					neighbour.g = current.g + 1
					neighbour.h = manhattan_distance(neighbour.position, end_node.position)
					neighbour.f = neighbour.g + neighbour.h
					if not neighbour in open:
						open.append(neighbour)
		

# AStarNode : AStarNode class used for the A* algorithm
class AStarNode():
		def __init__(self, parent, position):
				self.parent = parent
				self.position = position

				self.g = sys.maxsize
				self.h = 0
				self.f = 0

		# Returns the path from all parents to this node
		def path(self):
			path = []
			node = self
			while node:
					path.append(node.position)
					node = node.parent
			return path[::-1]

		def __eq__(self, other):
				return self.position == other.position

