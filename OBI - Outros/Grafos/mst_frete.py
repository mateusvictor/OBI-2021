# https://olimpiada.ic.unicamp.br/pratique/p2/2008/f2/frete/
def read_numbers():
	return tuple([int(x) for x in input().split()])


def find(x):
	if father[x] == x:
		return x

	father[x] = find(father[x])
	return father[x]


def union(x, y):
	x = find(x)
	y = find(y)

	if x == y:
		return

	if weight[x] < weight[y]:
		father[x] = y
	elif weight[y] < weight[x]:
		father[y] = x
	else:
		father[x] = father[y]
		weight[y] += 1

def union(x, y):
	father[find(x)] = find(y)


N, M = read_numbers()
father = [int(x) for x in range(N)]
weight = [0] * (N)
ans = 0
edges = []

for _ in range(M):
	edges.append(read_numbers())

edges.sort(key=lambda x: x[2])
print(edges)
for edge in edges:
	x, y, w = edge

	if find(x) != find(y):
		union(x, y)
		ans += w

print(ans)