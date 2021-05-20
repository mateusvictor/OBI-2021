# https://olimpiada.ic.unicamp.br/pratique/p2/2020/f3/rede/


N = int(input())
indices = []
ans = 0
last = None

for _ in range(N):
	indices.append(int(input()))


indices.sort(reverse=True)

for i, n in enumerate(indices):
	if n > ans:
		ans += 1

print(ans)
