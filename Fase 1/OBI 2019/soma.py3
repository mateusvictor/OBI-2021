# https://olimpiada.ic.unicamp.br/pratique/p2/2019/f1/soma/

def soma(nums, k):
	arr_sums = {0:1}

	soma = 0
	result = 0

	for n in nums:
		soma += n

		if (soma-k) in arr_sums:
			result += arr_sums[soma-k]

		arr_sums[soma] = arr_sums.get(soma, 0) + 1

	return result

N, K = [int(n) for n in input().split()]
nums = [int(n) for n in input().split()]

print(soma(nums, K))