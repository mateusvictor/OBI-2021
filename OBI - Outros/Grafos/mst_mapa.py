# https://olimpiada.ic.unicamp.br/pratique/p2/2011/f2/rmapa/

def read_numbers():
	return [int(n) for n in input().split()]


def find(x):
	if father[x] == x:
		return x
	father[x] = find(father[x])
	return father[x]


def join(x, y):
	father[find(x)] = y

N, M = read_numbers()
father = list(range(N+1))
edges = []
ans = 0


for _ in range(M):
	edges.append(read_numbers())

edges.sort(key=lambda x: x[2])

for edge in edges:
	x, y, w = edge

	if find(x) != find(y):
		join(x, y)
		ans += w

print(ans)
