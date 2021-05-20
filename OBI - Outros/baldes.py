# https://olimpiada.ic.unicamp.br/pratique/p2/2018/f3/baldes/

def read_numbers():
	return [int(x) for x in input().split()]

def solve(a, b):
	minimo = []
	maximo = []
	max_b = [float('-inf')]

	for x in range(a, b+1):
		minimo.append(min(baldes[x]))
		maximo.append(max(baldes[x]))
	
	

		


N, M = [int(x) for x in input().split()]
baldes = [[0]] + [[int(x)] for x in input().split()]
b_min

for balde in baldes:


for _ in range(M):
	op, p, i = read_numbers()

	if op == 1:
		baldes[i].append(p)
	else:
		solve(p, i)


print(baldes) 