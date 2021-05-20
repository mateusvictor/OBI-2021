# https://noic.com.br/materiais-informatica/curso/graphs-06/
def read_numbers():
	return [int(x) for x in input().split()]

N, M = read_numbers()
graph = [[] for _ in range(N)]
graus = [0] * N
lista = [] 
'''
9 5
1 2
3 2
2 6
8 5
5 7
'''
for _ in range(M):
	X, Y = read_numbers()

	graus[Y] += 1
	graph[X].append(Y)

for i in range(len(graus)):
	if graus[i] == 0:
		lista.append(i)
print(lista)

for actual in lista:
	for v in graph[actual]:
		graus[v] -= 1

		if graus[v] == 0:
			lista.append(v)

if not lista:
	print('*')
else:
	for n in lista:
		print(n)	