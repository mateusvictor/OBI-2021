def unique_paths(m, n):
	dp = [[0 for _ in range(n)] for _ in range(m)]
	print(dp)
	for row in range(m):
		for col in range(n):
			if row==0 and col==0:
				dp[row][col] = 1 
			else:
				dp[row][col] = dp[row-1][col] + dp[row][col-1]
			print(dp)
			
	return dp[m-1][n-1]

m, n = [int(x) for x in input().split()]
print(unique_paths(m, n))