# https://noic.com.br/materiais-informatica/comentario/obi-2020/fase1-turnob-p2/

# dp[i][j] = 1 + max([dp[j][k] for k in range(1, n) if dist[i][j] > dist[j][k]])


def compare(a, b):
	return dist(a[0], a[1]) < dist(b[0], b[1])


def dist(i, j):
	return (pares[i][0]-pares[j][0])**2 + (pares[i][1]-pares[j][1])

N = int(input())
pares = [(0, 0)]
par = []
mx = [0] * (N+1)

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(N):
	pares.append([int(x) for x in input().split()])


for i in range(N+1):
	for j in range(1, N+1):
		if i != j:
			par.append((i, j))

par.sort(key=lambda x: dist(x[0], x[1]))

i = 0
while i < len(par):
	j = i
	while j<len(par) and dist(par[i][0], par[i][1])==dist(par[j][0], par[j][1]):
		u = par[j][0]
		v = par[j][1]
		dp[u][v] = 1 + mx[v]
		j+=1

	print(dp)

	j = i
	while j<len(par) and dist(par[i][0], par[i][1]) == dist(par[j][0], par[j][1]):
		u = par[j][0]
		v = par[j][1]
		mx[u] = max(mx[u], dp[u][v])
		j+=1

	i = j

	print(mx)


print(max(dp[0]))