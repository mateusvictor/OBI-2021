import sys

sys.setrecursionlimit(10**6)

def grid_traveler(x, y):
	if memo[x][y]:
		return memo[x][y]

	elif x == 1 and y == 1:
		return 1
	elif x == 0 or y == 0:
		return 0

	memo[y][x] = memo[x][y] = grid_traveler(x-1, y) + grid_traveler(x, y-1)
	return memo[x][y]

x, y = 18, 18
memo = [[False for _ in range(y+1)] for _ in range(x+1)]

print(grid_traveler(x, y))