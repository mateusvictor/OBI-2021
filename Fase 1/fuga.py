def read_nums():
	return [int(n) for n in input().split()]

def dfs(L, C):
	grid[L][C] = 1
	custo += 1

	if L == X2 and C == Y2:
		resp = max(resp, custo)
	else:
		

	custo -= 1
	grid[L][C] = 1


custo = 0
resp = 0
N, M = read_nums()
X1, Y1 = read_nums()
X2, Y2 = read_nums()
grid = [[0 for _ in range(M)] for _ in range(N)]


