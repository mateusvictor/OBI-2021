# https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/ralouim/
from queue import Queue



def solution(n, w):
	queue = Queue()
	last = n
	temp = 1
	queue.put(n)
	print(n, end=' -> ')

	while not queue.empty():
		actual = queue.get()

		for vertex in pares[actual]:
			if vertex[0] > w:
				print(vertex[1], end=' -> ')
				w = vertex[0]
				last = actual
				temp += 1
				queue.put(vertex[1])
				break

	return temp


def dfs(n, w):
	temp = 0
	for vertex in pares[n]:
		if vertex[0] < w:
			temp = max(temp, dfs(vertex[1], vertex[0]))

	return temp


N = int(input())
coor = [[0, 0]]
pares = [[] for _ in range(N+1)]

initial = [float('inf'), float('inf')]
initial = [0] * (N+1)
ans = 0
par = {}

for _ in range(N):
	coor.append([int(x) for x in input().split()])

for i in range(N+1):
	for j in range(i+1, N+1):
		if i == j:
			continue
			
		dx = coor[i][0] - coor[j][0]
		dy = coor[i][1] - coor[j][1]

		if i == 0:
			initial[j] = dx**2 + dy**2
		else:
			pares[i].append([dx**2 + dy**2, j])
			pares[j].append([dx**2 + dy**2, i])
print(initial)
for p in pares:
	p.sort()

for i, p in enumerate(pares):
	print(f'{i} - {p}')

print(f'initial: {initial}')
for i in range(1, N+1):
	ans = solution(i, initial[i])
	print()
	print(ans)	
