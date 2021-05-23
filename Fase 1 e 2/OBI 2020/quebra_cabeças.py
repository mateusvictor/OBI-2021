# https://olimpiada.ic.unicamp.br/pratique/p2/2020/f2/quebra/

_ = int(input())
A = sorted([int(x) for x in input().split()][1:], reverse=True)
B = sorted([int(x) for x in input().split()][1:], reverse=True)

ans = 0

while len(A)>0 and len(B)>0:
	ans += B.pop(0) * A.pop(0)

print(ans)