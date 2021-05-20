# https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/fissura/
import sys


sys.setrecursionlimit(10**6)

def read_numbers():
	return [int(x) for x in input()]

def dfs(i, j):
	if i<0 or i>=N or j<0 or j>=N or grid[i][j]=='*' or grid[i][j]>F:
		return

	grid[i][j] = '*'

	for m in pos:
		for n in pos:
			if abs(m) != abs(n):
				dfs(i+n, j+m)


N, F = [int(x) for x in input().split()]
grid = []
pos = [-1, 0, 1]

for _ in range(N):
	grid.append(read_numbers())

dfs(0, 0)

for i in range(N):
	print(''.join(list(map(str, grid[i]))))
