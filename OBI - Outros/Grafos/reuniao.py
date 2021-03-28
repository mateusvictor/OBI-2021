# https://olimpiada.ic.unicamp.br/pratique/p2/2010/f1/reuniao/

from queue import PriorityQueue

def read_num():
	return [int(n) for n in input().split()]

def shortest_path(start):
	queue = PriorityQueue()
	queue.put((0, start))

	while not queue.empty():
		actual = queue.get()[1]

		if visited[actual]:
			continue

		visited[actual] = True

		for node in graph[actual].items():
			v, w = node

			if dist[v] > dist[actual]+w:
				dist[v] = dist[actual]+w
				queue.put((dist[v], v))

	return max(dist)

N, M = read_num()
graph = [{} for _ in range(N)]

for _ in range(M):
	U, V, W = read_num()
	graph[U][V] = min(W, graph[U].get(V, float('inf')))
	graph[V][U] = min(W, graph[V].get(U, float('inf')))

ans = float('inf')

for vertex in range(N):
	visited = [False] * N
	dist = [float('inf')] * N
	dist[vertex] = 0
	ans = min(ans, shortest_path(vertex))

print(ans)
