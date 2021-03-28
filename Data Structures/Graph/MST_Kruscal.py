class edge:
	def __init__(self, dist, x, y):
		self.dist = dist
		self.x = x
		self.y = y


def compare(a, b):
	return a.dist < b.dist


def find(x):
	while father[x] != x:
		x = father[x]

	return x


def join(a, b):
	a = find(a)
	b = find(b)

	if weight[a] < weight[b]:
		father[a] = b
	elif weight[b] < weight[a]:
		father[b] = a
	else:
		pai[a] = b
		peso[b] += 1

V, E = 6, 9

father = []
weight = []

edges = []
mst = []

