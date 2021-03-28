from math import sqrt

def distance(X1, Y1, X2, Y2):
	return sqrt((X1 - X2)**2 + (Y1 - Y2)**2)


while True:
	try:
		R1, X1, Y1, R2, X2, Y2 = [int(n) for n in input().split()]
		if R1 < R2:
			print('MORTO')
			continue

		if (X1, Y1) == (X2, Y2):
			print('RICO')
			continue

		d = distance(X1, Y1, X2, Y2)

		if R1 - d >= R2:
			print('RICO')
		else:
			print('MORTO')

	except EOFError:
		break

# Solução 2 - Menos codigo
#	- Circunferências internas: distance(C1, C2) <= R1-R2

from math import sqrt

def distance(X1, Y1, X2, Y2):
	return sqrt((X1 - X2)**2 + (Y1 - Y2)**2)


while True:
	try:
		R1, X1, Y1, R2, X2, Y2 = [int(n) for n in input().split()]

		if R1 - R2 >= distance(X1, Y1, X2, Y2):
			print('RICO')
		else:
			print('MORTO')

	except EOFError:
		break
