"""
V[i][w] = max(V[i-1][w], V[i-1][w-w[i]] + P[i])

O máximo entre:
	o lucro caso eu não inclua o item atual
	o lucro caso eu inclua item atual + o lucro máximo da capacidade restante (peso_permitido - peso[atual])
"""

def print_dp(dp):
	print('[')
	for e in dp:
		print(f'\t{e},')
	print(']')

def knapsack(capacity, value, weight):
	items = len(value)
	value.insert(0, 0)
	weight.insert(0, 0)

	dp = [[0 for _ in range(capacity+1)] for _ in range(items+1)]

	for p in range(1, items+1):
		for w in range(1, capacity+1):
			dp[p][w] = max(dp[p-1][w-weight[p]]+value[p] if w >= weight[p] else float('-inf'),
						   dp[p-1][w])

	print_dp(dp)
	included = [0] * (items+1)

	i = items
	j = capacity

	while i>0 and j>0:
		if dp[i][j] != dp[i-1][j]:
			included[i] = 1
			j -= weight[i]

		i -= 1

	print(included)

	return dp[len(value)-1][capacity]


k = 8
p = [1, 2, 5, 6]
w = [2, 3, 4, 5]

# k = 10
# p = [15, 23, 21, 16, 19, 18]
# w = [5, 4, 2, 4, 5, 2]

print(knapsack(k, p, w))