# https://noic.com.br/materiais-informatica/curso/graphs-03/

def matrix(dist):
	for i in range(N):
		print(dist[i])

def floyd_warshall():
	for k in range(N):
		for i in range(0, N):
			for j in range(0, N):
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


N, E = [int(n) for n in input().split()]
dist = [[0  for i in range(N)] for j in range(N)]

for i in range(E):
	a, b, w = [int(n) for n in input().split()]
	a -= 1
	b -= 1
	dist[a][b] = w
	dist[b][a] = w

matrix(dist)
print('\n')
floyd_warshall()
matrix(dist)