# https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/pandemia/

def read_numbers():
	return [int(x) for x in input().split()]

N, M = read_numbers()
I, R = read_numbers()
meets = [[]]
cont = set()
table = {n: False for n in range(1, N+1)}
table[I] = True
left = N


for _ in range(M):
	meets.append(read_numbers()[1:])



for i in range(R, M+1):
	for n in meets[i]:
		if table[n]:
			for n in meets[i]:
				cont.add(n)
				table[n] = True
			break

			
print(len(cont))