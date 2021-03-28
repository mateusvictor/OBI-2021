# https://olimpiada.ic.unicamp.br/pratique/p2/2017/f2/frete/
from queue import PriorityQueue

def read_numbers():
	return [int(n) for n in input().split()]

def shortest_path(start):
	queue = PriorityQueue()
	queue.put((0, start))

	while not queue.empty():
		actual = queue.get()[1]

		if visited[actual]:
			continue

		visited[actual] = True

		for node in graph[actual]:
			v, w = node

			if dist[v] > dist[actual]+w:
				dist[v] = dist[actual]+w
				queue.put((dist[v], v))

	return dist[-1]

N, M = read_numbers()
visited = [False] * (N)
dist = [float('inf')] * (N)
graph = [[] for _ in range(N)]

for _ in range(M):
	A, B, W = read_numbers()
	A -= 1
	B -= 1
	graph[A].append((B, W))
	graph[B].append((A, W))

dist[0] = 0
print(shortest_path(0))