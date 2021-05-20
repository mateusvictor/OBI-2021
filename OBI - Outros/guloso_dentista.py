# https://olimpiada.ic.unicamp.br/pratique/pj/2010/f2/dentista/

N = int(input())
consultas = []
end = 0
ans = 0

for _ in range(N):
	consultas.append(tuple(int(x) for x in input().split()))


consultas.sort(key=lambda x: x[1])

for consul in consultas:
	if consul[0] >= end:
		ans += 1
		end = consul[1]

print(ans)


