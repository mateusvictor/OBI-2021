# https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2513

def DFS(x):
	for vertex in adj_list[x]:
		if not visited[vertex]:
			visited[vertex] = True
			ans.append(1)
			DFS(vertex)


T = int(input())

for _ in range(T):
	N, M, L = [int(n) for n in input().split()]
	resp = 0

	adj_list = {i:[] for i in range(1, N+1)}

	for _ in range(M):
		x, y = [int(n) for n in input().split()]
		adj_list[x].append(y)

	for i in range(L):
		ans = [1]
		visited = {i:False for i in adj_list.keys()}
		start = int(input())
		visited[start] = True
		DFS(start)
		resp += sum(ans)

	print(resp)