# https://olimpiada.ic.unicamp.br/pratique/p1/2010/f1/times/

N, T = [int(n) for n in input().split()]
players = []

for _ in range(N):
	player, score = [n for n in input().split()]
	players.append((int(score), player))

players.sort(reverse=True)

clubs = [[] for _ in range(T)]
count = 0

for player in players:
	if count == T:
		count = 0

	clubs[count].append(player[1])
	count += 1

for i, club in enumerate(clubs):
	if i != 0:
		print()
		
	print('Time', i+1)
	print('\n'.join(sorted(club)))