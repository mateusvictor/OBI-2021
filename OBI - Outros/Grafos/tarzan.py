# https://olimpiada.ic.unicamp.br/pratique/p2/2012/f1/tarzan/
def read_numbers():
	return [int(n) for n in input().split()]

N, D = read_numbers()
grid = [[False for _ in range(5010)] for _ in range(5010)]

for _ in range(N):
	x, y = read_numbers()
	grid[x][y] = True

