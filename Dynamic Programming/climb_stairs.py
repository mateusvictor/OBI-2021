
def climb_stairs(n):
	if n == 1:
		return 1

	dp = [0, 1, 2] + [0] * (n-2)

	for i in range(3, n+1):
		dp[i] = dp[i-1][k-1] + dp[i-2][k-1]

	return dp[n]

print(climb_stairs(10000))