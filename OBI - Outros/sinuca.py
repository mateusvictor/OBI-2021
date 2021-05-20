# https://olimpiada.ic.unicamp.br/pratique/pj/2014/f2/sinuca/

N = int(input())
colors = [int(x) for x in input().split()]

for x in range(N-1, 0, -1):	
	a = [0] * N
	for n in range(0, x):
		a[n] = 1 if colors[n] == colors[n+1] else -1

	colors = a

print('branca' if colors[0] == -1 else 'preta')