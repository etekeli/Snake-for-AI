from Player import *
from Utility import *
from bots.AStar import AStar

# ZStar : AI that takes one of the longest path using the A* algorithm
# It Calculates a longest path from the head to the tail
# The path is recalculated when the snake travelled through the whole path
class ZStar(Player):
	def __init__(self):
		Player.__init__(self)
		self.name = "ZStar"
		self.path = list()
		self.astar = AStar()

	def decision(self, grid, snake, apple):
		if len(snake.body) < 4:
			return self.astar.decision(grid, snake, apple)
		else:
			# If there is no path or the snake has travelled through the whole path
			# Then we recalculate the path
			if self.path is None or len(self.path) <  random.randint(2, 9):
				# The snake's body parts are the obstacles
				maze = [[0 for col in range(grid.size)] for row in range(grid.size)]
				for item in snake.body:
					maze[item[0]][item[1]] = 1

				# The tail is not an obstacle, we have to reach it
				maze[snake.tail()[0]][snake.tail()[1]] = 0

				# Find a path
				self.path = self.z_star(maze, snake.head(), snake.tail(), apple)

			# To get the direction, we look at the difference between the beginning of the path and the snake's head
			if self.path:
				self.path.pop(0)
				next_step = self.path[0]
				direction = (next_step[0]-snake.head()[0], next_step[1]-snake.head()[1])
				return direction
			else:
				return self.astar.decision(grid, snake, apple) # No path found

	# Main Z* algorithm
	# The maze is a list of list
	# 0 represents a reachable area
	# 1 represents an obstacle
	def z_star(self, maze, start, end, apple):
		# Init lists and nodes
		open = [] # Nodes not treated yet
		closed = [] # Treated nodes
		start_node = ZStarNode(None, start) # Start node
		start_node.g = 0
		end_node = ZStarNode(None, end) # End node, the target
		open.append(start_node)

		paths = []
		while len(open) > 0:
			# Find the node with the highest f cost
			current = open[0]
			current_index = 0
			for index, item in enumerate(open):
					if item.f > current.f:
							current = item
							current_index = index

			# Remove current from open and add it to closed
			open.pop(current_index)
			closed.append(current)

			# If the current node is the target, we add it to the path list
			if current == end_node:
					paths.append(current.path())

			# Discover neighbours of current
			self.discover_neighbours(maze, current, open, closed, end_node)

		return self.chose_path(paths, apple)


	# Discovers and manages neighbours of current 
	def discover_neighbours(self, maze, current, open, closed, end_node):
		# Neighbours
		for direction in [d.value for d in Directions]:
				neighbour = ZStarNode(current, (current.position[0] + direction[0], current.position[1] + direction[1]))

				# Continue to the next neighbour if neighbour is in closed or is not reachable
				if (neighbour in closed 
					or neighbour.position[0] > (len(maze) - 1) 
					or neighbour.position[0] < 0 
					or neighbour.position[1] > (len(maze[0]) -1) 
					or neighbour.position[1] < 0
					or maze[neighbour.position[0]][neighbour.position[1]]):
						continue

				# Set costs
				neighbour.g = current.g + 2
				neighbour.h = manhattan_distance(neighbour.position, end_node.position)
				neighbour.f = neighbour.g + neighbour.h

				# Manage the neighbour
				if not neighbour in open:
					open.append(neighbour)
				else:
					for index, item in enumerate(open):
						if item == neighbour:
							if neighbour.g >= item.g:
								open.pop(index)
							open.append(neighbour)
							break
	
	# Choses one of the longest paths,
	# choses the one with the apple in priority
	def chose_path(self, paths, apple):
		longest_path = paths[0]
		longest_paths = []
		for path in paths:
			if len(path) > len(longest_path):
				longest_path = path
		for path in paths:
			if len(longest_path) == len(path):
				longest_paths.append(path)
		for path in longest_paths:
			if apple.position in path:
				return  path
		return random.choice(longest_paths)
	

# ZStarNode : ZStarNode class used for the A* algorithm
class ZStarNode():
		def __init__(self, parent, position):
				self.parent = parent
				self.position = position

				self.g = 0
				self.h = 0
				self.f = 0

		def path(self):
			path = []
			node = self
			while node:
					path.append(node.position)
					node = node.parent
			return path[::-1]

		def __eq__(self, other):
				return self.position == other.position

