# https://olimpiada.ic.unicamp.br/pratique/pj/2011/f2/gincana/

def find(x):
	while father[x] != x:
		x = father[x]
	return x


def join(x, y):
	x = find(x)
	y = find(y)
	
	if x == y:
		return 

	if weight

	father[find(x)] = find(y)


N, K  = [int(n) for n in input().split()]
father = [i for i in range(0, N+1)]
weight = [0] * (N+1)

for _ in range(K):
	F1, F2 = [int(n) for n in input().split()]
	join(F1, F2)
	print(father)

ans = 0
for i in range(1, N+1):
	if find(i) == i:
		ans += 1

print(ans)
