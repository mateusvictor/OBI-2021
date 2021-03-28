from random import randint
def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]

		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
		print(arr)


arr = [randint(1, 2980) for _ in range(10)]

insertion_sort(arr)
print(f'Sorted array: {arr}')