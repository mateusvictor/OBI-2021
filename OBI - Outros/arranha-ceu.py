# https://olimpiada.ic.unicamp.br/pratique/p2/2017/f3/arranhaceu/

N, Q = [int(n) for n in input().split()]
andar = [int(n) for n in input().split()]
prefix = [andar[0]] + [0] * (N - 1)
length = len

for i in range(1, N):	
	prefix[i] = prefix[i-1] + andar[i]


# [30, 2,   0, 42, 10, 11, 11,    9]
# [30, 32, 32, 74, 84, 95, 106, 115]

add = [0] * N
for i in range(Q):
	querie = [int(n) for n in input().split()]

	if querie[0] == 1:
		print(prefix[querie[1]-1] + add[querie[1]-1])
	else:
		add[querie[1]-1] += -1 * (prefix[querie[1]-1] - querie[2])