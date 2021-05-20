from random import randint

def merge_sort(arr):
	if len(arr) < 2:
		return
	
	mid = len(arr) // 2

	left = arr[:mid]
	right = arr[mid:]

	merge_sort(left)
	merge_sort(right)

	i = j = k = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1

	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1

	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1
	 	 
	return arr

	
arr = [38, 27, 41, 3, 9, 82, 10]
print(f'Sorted array: {merge_sort(arr)}')
print(arr)
arr = [randint(1, 10000) for _ in range(1000)]
