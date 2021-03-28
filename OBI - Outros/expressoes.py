# https://olimpiada.ic.unicamp.br/pratique/p2/2011/f2/expressoes/

stack = []
table = {')':'(', ']':'[', '}':'{'}
N = int(input())

for i in range(N):
	stack = []
	test = str(input())

	for c in test:
		if stack and table.get(c, '') == stack[-1]:
			stack.pop()
		else:
			stack.append(c)

	if stack:
		print('N')
	else:
		print('S')

