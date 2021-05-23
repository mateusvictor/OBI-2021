# https://olimpiada.ic.unicamp.br/pratique/p2/2020/f2/formiga/

def read_numbers():
	return [int(x) for x in input().split()]


def max_saloes(start):
	queue = [start]
	ans = -1

	while len(queue) > 0:
		actual = queue.pop(0)

		if visited[actual]:
			continue

		ans += 1
		visited[actual] = True

		for vertex in graph[actual]:
			queue.append(vertex)

	return ans



S, T, P = read_numbers()
visited = [False] * (S+1)
heights = [None] + read_numbers()
graph = [None] + [[] for _ in range(S)]


for _ in range(T):
	A, B = read_numbers()

	if heights[A] > heights[B]:
		graph[A].append(B)
	else:
		graph[B].append(A)


print(max_saloes(P))
