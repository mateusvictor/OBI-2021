# https://olimpiada.ic.unicamp.br/pratique/p2/2009/f1/pontes/
from queue import PriorityQueue


def shortest_path(start, end):
	queue = PriorityQueue()
	queue.put((0, start))

	while not queue.empty():
		u = queue.get()[1]

		if visited[u]:
			continue

		visited[u] = True

		for node in adj_list[u]:
			v, w = node

			if dist[v] > dist[u]+w:
				dist[v] = dist[u]+w
				queue.put((dist[v], v))

	return dist[end]

N, M = [int(n) for n in input().split()]
adj_list = [[] for _ in range(N+2)]
visited = [False for _ in range(N+2)]
dist = [float('inf') for _ in range(N+2)]
dist[0] = 0

for _ in range(M):
	try:
		S, E, W = [int(n) for n in input().split()]
		adj_list[S].append((E, W))
		adj_list[E].append((S, W))
	except:
		pass
		
print(shortest_path(0, N+1))
