N = int(input())
T = list(map(int, input().split()))
P = int(input())
M = int(input())

if T.count(1) <= P and T.count(2) <= M:
	print('S')
else:
	print('N')
