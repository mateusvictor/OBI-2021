# https://olimpiada.ic.unicamp.br/pratique/p2/2018/f2/elevador/

def read_numbers():
	return [int(x) for x in input().split()]

N = int(input())
boxes = sorted(read_numbers())
up = 0
ans = 'S'

for box in boxes:
	if abs(up-box) > 8:
		ans = 'N'
		break

	up = box

print(ans)
