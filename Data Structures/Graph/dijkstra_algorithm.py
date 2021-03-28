from queue import PriorityQueue


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