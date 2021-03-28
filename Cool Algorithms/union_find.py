# Union Find - https://noic.com.br/materiais-informatica/curso/data-structures-08/

def find(x):
	while father[x] != x:
		x = father[x]
	return x

def f(x):
	if father[x] == x:
		return x
	return find(father[x])


def join(x, y):
	father[find(x)] = find(y)


N, K = [int(n) for n in input().split()]

father = [i for i in range(0, N+1)]

for _ in range(K):
	op, bank1, bank2 = [int(n) if n.isnumeric() else n for n in input().split()]

	if op == 'F':
		join(bank1, bank2)
	else:
		if find(bank1) == find(bank2):
			print('S')
		else: 
			print('N')	