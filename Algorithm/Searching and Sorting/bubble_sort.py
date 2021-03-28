from random import randint

def bubble_sort(arr):
	for i in range(0, len(arr)):
		for j in range(i+1, len(arr)):
			if arr[j] < arr[i]:
				arr[j], arr[i] = arr[i], arr[j]
	return arr

arr = [randint(1, 1823) for _ in range(19)]
print(f'Sorted arry: {bubble_sort(arr)}')