# https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/promocao/
from queue import Queue

def dfs(v, parent):
	maior_branco = maior_preto = 0

	for vertex in graph[v]:
		if vertex[0] == parent:
			continue

		if vertex[1] == 1:
			maior_branco = max(maior_branco, dfs(vertex[0], v)[1])
		else:
			maior_preto = max(maior_preto, dfs(vertex[0], v)[0])

	ans[0] = max(ans[0], maior_branco + maior_preto + 1)

	return [maior_branco+1, maior_preto+1]



N = int(input())
graph = [None] + [[] for _ in range(N)]

father = [None] + list(range(1, N+1))


for _ in range(N-1):
	A, B, C = [int(x) for x in input().split()]
	graph[A].append((B, C))
	graph[B].append((A, C))

ans = [0]
dfs(1, -1)
print(ans)