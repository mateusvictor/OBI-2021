def selection_sort(arr):
	for i in range(len(arr)):
		min_index = i

		# Find the  minimum element in remaining unsorted arr
		for j in range(i + 1, len(arr)):	
			if arr[min_index] > arr[j]:
				min_index = j

		# Swap the found minimum element with the first element
		arr[i], arr[min_index] = arr[min_index], arr[i]
		print(arr)

	return arr

arr = [64, 25, 12, 22, 11]
print(f'Sorted array: {selection_sort(arr)}')