class Edge:
	def __init__(self, n_from, n_to, weight):
		self.n_from = n_from
		self.n_to = n_to
		self.weight = weight


def find(x):
	if father[x] == x:
		return x

	father[x] = find(father[x])

	return father[x]

def join(x, y):
	x = find(x)
	y = find(y)

	if x == y:
		return 

	if weight[x] < weight[y]:
		father[x] = y

	elif weight[y] < weight[x]:
		father[y] = x
	else:
		father[x] = y
		weight[y] += 1


graph = [
	[],
	[(6, 10), (2, 28)],
	[(7, 14), (3, 16), (1, 28)],
	[(4, 12), (2, 16)],
	[(3, 12), (7, 18), (5, 22)],
	[(4, 22), (7, 24), (6, 25)],
	[(1, 10), (5, 25)],
]

nodes = 7
edges = [(1, 6, 10), (1, 2, 28), (2, 7, 14), (2, 3, 16),
		(3, 4, 12), (4, 7, 18), (4, 5, 22), (5, 7, 24), (5, 6, 25)]


edges = sorted(edges, key= lambda x:x[2])
visited = [False] * (nodes+1)
father = [i for i in range(nodes+1)]
weight = [0] * (nodes+1)
soma = 0

for edge in edges:

	x, y, z = edge

	if find(x) != find(y):
		join(x, y)
		soma += z

	
print(soma)