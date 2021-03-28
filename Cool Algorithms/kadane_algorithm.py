def kadanes_algorithm(arr):
	max_current = max_global = arr[0]

	for i in range(1, len(arr)):
		max_current = max(arr[i], max_current + arr[i])
		if max_current > max_global:
			max_global = max_current
	return max_global

# Solution 2: codewars
def max_sequence(arr):
	max_global = max_current = 0

	for x in arr:
		max_current += x
		max_current = max(max_current, 0)
		max_global = max(max_current, max_global)

	return max_global


arr = [-2, 3, 2, -1]

print(kadanes_algorithm(arr), max_sequence(arr))