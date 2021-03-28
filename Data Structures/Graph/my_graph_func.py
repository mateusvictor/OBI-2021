from queue import Queue


def add_edge(start, end):
	adj_list[start] = adj_list.get(start, []) + [end]


def print_graph():
	for node, chields in adj_list.items():
		print(f'{node} -> {chields}')

def length():
	return len(adj_list)

def DFS(x):
	path.append(x)
	for vertex in adj_list[x]:
		if not visited[vertex]:
			visited[vertex] = True
			DFS(vertex)

def BFS(x):
	queue = Queue()
	queue.put(x)
	path = []

	while not queue.empty():
		temp = queue.get()
		path.append(temp)

		for vertex in adj_list[temp]:
			if not visited[vertex]:
				visited[vertex] = True
				queue.put(vertex)

	return path


adj_list = {}

routes = [
	(1, 2), (1, 4), (2, 1), (2, 3), 
	(2, 6), (3, 2), (3, 4), (3, 6),
	(4, 1), (4, 3), (5, 6), (6, 2), 
	(6, 3), (6, 5), (7, 8), (8, 7), 
	(9, 9),
]

for route in routes:
	add_edge(route[0], route[1])

"""
print('''	1: [2, 4], 
	2: [1, 3, 6],
	3: [2, 4, 6],
	4: [1, 3],
	5: [6],
	6: [2, 3, 5],
	7: [8],
	8: [7],
	9: [None]''')
"""

path = []
visited = {node:False for node in adj_list.keys()}
start = int(input())
visited[start] = True
#DFS(start)
path = BFS(start)
print(path)