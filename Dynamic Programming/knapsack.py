# https://www.youtube.com/watch?v=xOlhR_2QCXY
# https://noic.com.br/materiais-informatica/curso/techniques-03/

def naive_solution(item, capacity):
	if item == 0 or capacity == 0:
		result = 0
	elif weight[item] > capacity:
		return naive_solution(item-1, capacity)
	else:
		temp1 = naive_solution(item-1, capacity)
		temp2 = value[item] + naive_solution(item-1, capacity-weight[item])
		result = max(temp1, temp2)

	return result

def knapsack(item, capacity):
	if table[item][capacity]:
		return table[item][capacity]

	if item == 0 or capacity == 0:
		result = 0
	elif weight[item] > capacity:
		result = knapsack(item-1, capacity)
	else:
		temp1 = knapsack(item-1, capacity)
		temp2 = value[item] + knapsack(item-1, capacity-weight[item])
		result = max(temp1, temp2)

	table[item][capacity] = result
	return result

N, C = 4, 8
length = C+1
weight = [None, 1, 2, 5, 6]
value = [None, 2, 3, 4, 5]
table = [[False for _ in range(length)] for _ in range(length)]
"""
N, C = 5, 10
length = N+6
weight = [None, 1, 2, 4, 2, 5]
value = [None, 5, 3, 5, 3, 2]
table = [[False for _ in range(length)] for _ in range(length)]
"""
# print(naive_solution(N, C))
print(knapsack(N, C))