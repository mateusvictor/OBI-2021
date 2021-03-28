def DFS(x):
	for vertex in adj_list[x]:
		if not visited[vertex]:
			visited[vertex] = True
			DFS(vertex)
 

N, M = [int(n) for n in input().split()]
adj_list = {i:[] for i in range(1, N+1)}

for route in range(M):
	x, y = [int(n) for n in input().split()]
	adj_list[x].append(y)
	adj_list[y].append(x)

visited = {node:False for node in range(1, N+1)}

ans = 0

for i in range(1, N+1):
	if not visited[i]:
		visited[i] = True
		ans += 1
		DFS(i)

print(ans)
