
def coin_change(nums, k):
	dp = [1] + [0]*k

	for i in range(1, k+1):
		for n in nums:
			dp[i] += dp[i-n]


	return dp[-1]



nums = [1, 2, 3]
print(coin_change(nums, 4))