import sys

sys.setrecursionlimit(10**5)

def fib(n, memo={}):
	if n in memo: 
		return memo[n]
	if n <= 2:
		return 1

	memo[n] = fib(n-1, memo) + fib(n-2, memo)
	return memo[n]


def cool_fib(n):
	lista = [0, 1, 1]
	a = b = 1

	for x in range(3, n+1):
		b, a = b+a, b
		
		# lista.append(lista[x-1] + lista[x-2])

	return a, b

memo = [0, 1, 1]
print(fib(500))
