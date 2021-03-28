from queue import Queue 

def get_winner(n):
	if n == 0:
		return winners.get()

	for i in range(n):
		teams = [winners.get(), winners.get()]
		score = [int(n) for n in input().split()]
		winner = teams[score.index(max(score))]
		winners.put(winner)

	return get_winner(n//2)

winners = Queue()

for team in 'ABCDEFGHIJKLMNOP':
	winners.put(team)

print(get_winner(8))