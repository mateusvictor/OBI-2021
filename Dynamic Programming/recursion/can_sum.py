def can_sum(target, numbers, memo={}):
	if target in memo:
		return memo[target]
	if target == 0:
		return True
	if target < 0:
		return False

	for number in numbers:
		remainder = target - number

		if can_sum(remainder, numbers, memo):
			memo[target] = True
			return True
	memo[target] = False

	return False

def can_sum(target, numbers):
	table = [False]*(target+1)
	table[0] = True

	

print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(300, [7, 14]))
