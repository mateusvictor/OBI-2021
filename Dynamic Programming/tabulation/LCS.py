def LCS(A, B):
	dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

	for i in range(1, len(A)+1):
		for j in range(1, len(B)+1):
			if A[i-1] == B[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i][j-1], dp[i-1][j])

	

	i = len(A)
	j = len(B)
	ans = []

	while i>0 and j>0:
		if dp[i][j] == dp[i][j-1]:
			j -= 1
		elif dp[i][j] == dp[i-1][j]:
			i -= 1
		else:
			ans.insert(0, A[i-1])
			i -= 1
			j -= 1

	print(''.join(ans))
	return dp[-1][-1]



A = 'abcdeghij'
B = 'ecdgi'

A = 'stone'
B = 'longest'

print(LCS(A, B))
