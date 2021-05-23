
def knapsack(capacity, value, weight):
	value.insert(0, 0)
	weight.insert(0, 0)
	dp = [[0 for _ in range(capacity+1)] for _ in range(len(value))]

	
	for p in range(1, len(value)):
		for w in range(1, capacity+1):
			dp[p][w] = max(
				dp[p-1][w], 
				dp[p-1][w-weight[p]] + value[p] if w >= weight[p] else float('-inf'))

	return dp[len(value)-1][capacity]

while True:
	n = int(input())

	if n == 0:
		break

	k = int(input())
	value = []
	weight = []

	for _ in range(n):
		temp = [int(x) for x in input().split()]
		value.append(temp[0])
		weight.append(temp[1])

	print(knapsack(k, value, weight), 'min.')