from queue import Queue
import sys

sys.setrecursionlimit(10**6	)

def read_numbers():
	return [int(x) for x in input().split()]

def bfs(node):
	queue = Queue()
	queue.put(node)

	while not queue.empty():
		u = queue.get()

		for vertex in graph[u]:
			if not visited[vertex]:
				visited[vertex] = True
				queue.put(vertex)

def dfs(node):
	for v in graph[node]:
		if not visited[v]:
			visited[v] = True

			dfs(v)

N, M = read_numbers()
graph = [None] + [[] for _ in range(N)] 
visited = [False] * (N+1)


for _ in range(M):
	x, y = read_numbers()
	graph[x].append(y)
	graph[y].append(x)

family = 0

for node in range(1, N+1):
	if not visited[node]:
		visited[node] = True

		bfs(node)
		family += 1

print(family)		
