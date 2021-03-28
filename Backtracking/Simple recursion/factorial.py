def factorial_recursive(n):
	if n <= 1:
		return 1
	else:
		return n * factorial_recursive(n-1)

def factorial_iterative(n):
	ans = 1

	for i in range(1, n+1):
		ans *= i

	return ans

n = 100

#print(factorial_recursive(n))
print(factorial_iterative(n))