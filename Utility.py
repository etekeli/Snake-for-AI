import math

# Heuristics
# http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html

# Manhattan disctance
def manhattan_distance(p, q):
	dx = abs(p[0] - q[0])
	dy = abs(p[1] - q[1])
	return dx + dy

# Euclidian distance
def euclidian_distance(p, q):
	dx = abs(p[0] - q[0])
	dy = abs(p[1] - q[1])
	return math.sqrt(dx * dx + dy * dy)

# Euclidian distance without square
# This doesn't give a shorter path, that's why 
# it's not recommended in the article.
# However, it's better not to take the shortest path
# when the snake gets bigger. That's why this one
# gives better performances than the second heuristic
def euclidian_distance2(p, q):
	dx = abs(p[0] - q[0])
	dy = abs(p[1] - q[1])
	return dx * dx + dy * dy