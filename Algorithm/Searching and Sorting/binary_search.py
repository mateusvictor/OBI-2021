from datetime import datetime
from random import randint

def binary_search(arr, item):
	begin = 0
	end = len(arr) - 1

	while begin <= end:

		middle = begin + (end - begin ) // 2
		
		if arr[middle] == item:
			return middle

		elif arr[middle] < item:
			begin = middle + 1

		elif arr[middle] > item:
			end = middle - 1

	return -1

def recursive_binary_search(arr, begin, end, item):
	if begin <= end:
		middle = begin + (end - begin) // 2

		if arr[middle] == item:
			return middle

		elif arr[middle] > item:
			return recursive_binary_search(arr, begin, middle - 1, item)

		elif arr[middle] < item:
			return recursive_binary_search(arr, middle + 1, end, item)
	else:
		return -1

arr = sorted([randint(1, 1000) for _ in range(100)])
print(arr)

item = int(input('Item to search: '))

#result = binary_search(arr, item)
result = recursive_binary_search(arr, 0, len(arr) - 1, item)

if result == -1:
	print('Item not found in the array :(')
else:
	print(f'Item {item} found at index {result}.')

