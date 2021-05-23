def how_sum(target, numbers, memo=None):
	if memo is None:
		memo = []

	if target in memo:
		return memo[target]
	if target == 0:
		return []
	if target < 0:
		return None

	for number in numbers:
		remainder = target - number
		result = how_sum(remainder, numbers, memo)

		if result is not None:
			memo[target] = result + [number]
			
			return memo[target]

	memo[target] = None
	return None

print(how_sum(300, [7, 14], {}))
print(how_sum(8, [2, 3, 5], {}))
print(how_sum(7, [2, 4], {}))
