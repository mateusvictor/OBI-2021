def merge_arrays(arr1, arr2):
	i = j = k = 0
	len1 = len(arr1)
	len2 = len(arr2)

	result = [0 for _ in range(len1+len2)]

	while i < len1 and j < len2:
		if arr1[i] < arr2[j]:
			result[k] = arr1[i]
			k += 1
			i += 1
		else:
			result[k] = arr2[j]
			k += 1
			j += 1

	while i < len1:
		result[k] = arr1[i]
		k += 1
		i += 1

	while j < len2:
		result[k] = arr2[j]
		k += 1
		j += 1

	return result


arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]

print(f'Two sorted arrays merged: {merge_sorted(arr1, arr2)}')