# https://olimpiada.ic.unicamp.br/pratique/p2/2008/f1/lanche/

from queue import PriorityQueue


def shortest_path(start):
	queue = PriorityQueue()
	queue.put((0, start))

	while not queue.empty():
		actual = queue.get()[1]

		if visited[actual]:
			continue

		visited[actual] = True
		
		for node in adj_list[actual]:
			v, w = node
			if dist[v] > dist[actual]+w:
				dist[v] = dist[actual]+w
				queue.put((dist[v], v))
	return max(dist)

S, C = [int(n) for n in input().split()]
adj_list = [[] for n in range(S)]
ans = []

for _ in range(C):
	try:
		A, B, W = [int(n) for n in input().split()]
	except:
		continue
	A -= 1
	B -= 1
	adj_list[A].append((B, W))
	adj_list[B].append((A, W))

min_dist = float('inf')

for i in range(S):
	dist = [float('inf') for n in range(S)]
	dist[i] = 0
	visited = [False for _ in range(S)]
	min_dist = min(min_dist, shortest_path(i))

print(min_dist)