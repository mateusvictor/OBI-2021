# https://www.urionlinejudge.com.br/judge/pt/problems/view/1148
# AAAAAAAAA
from queue import Queue


def bfs(start, end):
	queue = Queue()
	queue.put((start, 0))

	while not queue.empty():
		actual, weight = queue.get()

		if visited[actual]:
			continue

		visited[actual] = True

		for vertex in graph[actual]:
			v, w = vertex

			if v == end:
				dist[end] = min(dist[actual], dist[v]+w)

			if
			elif dist[v] > dist[actual]+w:
				dist[v] = dist[actual] + w 
				queue.put((v, dist[v]))


	return dist[end]

def read_numbers():
	return [int(n) for n in input().split()]

N, E = read_numbers()

graph = [[] for n in range(N+1)]

for _ in range(E):
	A, B, W = read_numbers()
	graph[A].append((B, W))

Q = int(input())

for _ in range(Q):
	visited = [False] * (N+1)
	dist = [float('inf')] * (N+1)
	S, E = read_numbers()
	dist[S] = 0
	resposta = bfs(S, E)
	print(resposta)
