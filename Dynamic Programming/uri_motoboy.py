# https://www.urionlinejudge.com.br/judge/pt/problems/view/1286

def solution(item, capacity):
	if table[item][capacity]:
		return table[item][capacity]

	if item==0 or capacity==0:
		result = 0
	elif w[item] > capacity:
		return solution(item-1, capacity)
	else:
		nao_coloca = solution(item-1, capacity)
		coloca = v[item] + solution(item-1, capacity-w[item])
		result = max(nao_coloca, coloca)

	table[item][capacity] = result
	return result


while True:
	N = int(input())
	if N == 0:
		break

	P = int(input())
	entregas = []
	v = [None]
	w = [None]
	table = [[False for _ in range(P+1)] for _ in range(N+1)]

	for _ in range(N):
		entrega = [int(x) for x in input().split()]
		v.append(entrega[0]), w.append(entrega[1])

	print(str(solution(N, P)) + ' min.')
