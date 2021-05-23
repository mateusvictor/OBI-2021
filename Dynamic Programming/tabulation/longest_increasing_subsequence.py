 # LIS[n] =  + max(LIS[k] | k < n, A[k] < A[n])

def LIS():
	LIS = [1] * len(array)

	for i in range(1, len(array)):
		subproblems = [LIS[k] for k in range(i) if array[k] < array[i]]
		LIS[i] = 1 + max(subproblems, default=0)
		
	return max(LIS, default=0)

array = [5, 2, 8, 6, 3, 6, 9, 5]
print(LIS())