# https://olimpiada.ic.unicamp.br/pratique/pj/2017/f3/onibus/
from queue import Queue

def read_numbers():
	return [int(x) for x in input().split()]

def shortest_path(start, end):
	queue = Queue()
	queue.put((0, start))
	dist[start] = 0

	while not queue.empty():

		actual = queue.get()[1]

		if visited[actual]:
			continue

		visited[actual] = True

		for vertex in graph[actual]:
			if dist[vertex] > dist[actual]+1:
				dist[vertex] = dist[actual]+1
				queue.put((dist[vertex], vertex))

	return dist[end]


N, S, E = read_numbers()
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
dist = [float('inf')] * (N+1)

for _ in range(N-1):
	A, B = read_numbers()
	graph[A].append(B)
	graph[B].append(A)

print(shortest_path(S, E))