
def LCS(i, j):
	if dp[i][j]:
		return dp[i][j]

	if A[i]=='0' or B[j]=='0':
		result = 0
	elif A[i]==B[j]:
		result = 1 + LCS(i+1, j+1)
	else:
		result = max(LCS(i+1, j), LCS(i, j+1))

	dp[i][j] = result
	return result


# A = 'bd0'
# B = 'abcd0'

A = 'abcdeghij0'
B = 'ecdgi0'

dp = [[False for _ in range(len(B)+1)] for _ in range(len(A)+1)]
rp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

print(LCS(0, 0))