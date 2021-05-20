N = int(input())
melhor = [0 for _ in range(N + 1)]
pmelhor = [0 for _ in range(N + 1)]
pdist = [0 for _ in range(N + 1)]

pontos = [[0, 0]]

for i in range(N):
	X, Y = [int(cor) for cor in input().split()]
	pontos.append([X, Y])


pares = []
for A in range(N + 1):
	for B in range(A + 1, N + 1):
		dX = pontos[A][0] - pontos[B][0]
		dY = pontos[A][1] - pontos[B][1]
		#print(f"PARES : {pontos[A]} e {pontos[B]}")
		temp = [dX ** 2 + dY ** 2, A, B]
		#print(temp, '\n\n')
		pares.append(temp)

pares.sort()
print(pares)

for par in pares:
	print("PAR: ", par)
	dist = par[0]
	A = par[1]
	B = par[2]
	print("PDIST", pdist)
	print("MELHOR", melhor)
	print("PMELHOR", pmelhor)

	if dist != pdist[A]:
		print(f"IF 1: {dist} != {pdist[A]}")
		pdist[A] = dist
		pmelhor[A] = melhor[A]

	if dist != pdist[B]:
		print(f"IF 2: {dist} != {pdist[B]}")
		pdist[B] = dist
		pmelhor[B] = melhor[B]

	if A == 0:
		print(f"IF 3: {A} == 0")
		melhor[A] = max(melhor[A], pmelhor[B])
	else:
		melhor[A] = max(melhor[A], 1+pmelhor[B])
		melhor[B] = max(melhor[B], 1+pmelhor[A])

	print('\n\n')
print(1+melhor[0])