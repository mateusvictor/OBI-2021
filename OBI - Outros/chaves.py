# https://olimpiada.ic.unicamp.br/pratique/p2/2016/f1/chaves/

stack = []
N = int(input())

expression = ''
for i in range(N):
	expression += str(input())

ans = 0
for c in expression:
	if c not in '{}':
		continue

	if c == '{':
		ans += 1
	else:
		ans -= 1

if ans != 0:
	print('N')
else:
	print('S')

