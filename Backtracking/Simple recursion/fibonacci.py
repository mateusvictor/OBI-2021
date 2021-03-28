def fibonacci_recursive():
	if n == 0:
		return 0;
	if n <= 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_iterative(n):
	arr = [0, 1]

	for i in range(2, n+1):
		arr.append(arr[i-1] + arr[i-2])

	return arr[-1]

n = 100
print(fibonacci_iterative(n))

