N, M = [int(n) for n in input().split()]
chuva = [list(input()) for _ in range(N)]

for i in range(N):
	for j in range(M):
		if chuva[i][j] != '.':
			continue
		if i-1>=0 and chuva[i-1][j]=='o':
			chuva[i][j] = 'o' 
		if (j-1>=0 and (i+1) < N and chuva[i][j-1] == 'o' and chuva[i+1][j-1] == '#') or (j+1<M and (i+1) < M and chuva[i][j+1] == 'o' and chuva[i+1][j+1] == '#'):
			chuva[i][j] = 'o';

	for j in range(M-1, -1, -1):
		if chuva[i][j] != '.':
			continue
		if (j-1>=0 and (i+1) < N and chuva[i][j-1] == 'o' and chuva[i+1][j-1] == '#') or (j+1<M and (i+1) < N and chuva[i][j+1] == 'o' and chuva[i+1][j+1] == '#'):
			chuva[i][j] = 'o';

print('\n'.join([''.join(chuva[i]) for i in range(N)]))