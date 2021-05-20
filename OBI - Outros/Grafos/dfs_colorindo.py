# https://olimpiada.ic.unicamp.br/pratique/p1/2011/f2/colorir/
import sys


sys.setrecursionlimit(10**8)

def read_numbers():
	return [int(x) for x in input().split()]

def dfs(i, j):
	if i<1 or i>N or j<1 or j>M or grid[i][j]:
		return

	grid[i][j] = True
	soma[0] += 1

	for x in range(i-1, i+2):
		for y in range(j-1, j+2):
			dfs(x, y)


N, M, X, Y, K = read_numbers()
grid = [[False for _ in range(M+2)] for _ in range(N+2)]

soma = [0]


for _ in range(K):
	A, B = read_numbers()

	grid[A][B] = True

dfs(X, Y)
print(soma[0])