# Union Find - https://noic.com.br/materiais-informatica/curso/data-structures-08/

def find(x):
	while father[x] != x:
		x = father[x]
	return x

def find(x):
	if father[x] == x:
		return x
	
	father[x]=find(father[x])
	return father[x]


def join(x, y):
	x = find(x)
	y = find(y);

	if x == y:
		return

	if weight[x] < weight[y]:
		father[x] = y
	elif weight[x] > weight[y]:
		father[y] = x

	if weight[x] == weight[y]:
		father[x] = y
		weight[y] += 1


N, K = [int(n) for n in input().split()]

father = [i for i in range(0, N+1)]
weight = [i for i in range(0, N+1)]


for _ in range(K):
	op, bank1, bank2 = [int(n) if n.isnumeric() else n for n in input().split()]

	if op == 'F':
		join(bank1, bank2)
	else:
		if find(bank1) == find(bank2):
			print('S')
		else: 
			print('N')	