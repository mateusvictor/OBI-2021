def first_occurence(array, x):
	result = -1
	begin = 0
	end = len(array)-1

	while begin <= end:
		mid = (begin+end) // 2

		if array[mid] == x:
			result = mid
			end = mid-1

		elif array[mid] > x:
			begin = mid + 1

		else:
			end = mid - 1

	return result


def last_occurence(array, x):
	result = -1
	begin = 0
	end = len(array) - 1

	while begin <= end:
		mid = (begin + end) // 2

		if array[mid] == x:
			result = mid
			begin = mid + 1

		elif array[mid] > x:
			end = mid - 1

		else:
			begin = mid + 1

	return result


def how_many_occurences(array, x):
	 



query = 10
array = [2, 4, 10, 10, 10, 18, 20]
print(f'Index of first occurence of {query} is {first_occurence(array, query)}')
print(f'Index of last occurence of {query} is {last_occurence(array, query)}')