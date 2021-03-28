def missing_number(arr):
	arr = sorted(arr)

	for i in range(len(arr)):
		if i+1 != arr[i]:
			return i+1 


def missing_number_2(arr):
	total = (len(arr)+1) * (len(arr)+2) // 2
	return total - sum(arr)


arr = [1, 2, 4, 6, 3, 7, 8]
print(f'Missing number in the array {arr} is {missing_number_2(arr)}')