# https://olimpiada.ic.unicamp.br/pratique/pj/2017/f3/gomoku/


grid = []
for _ in range(15):
	grid.append([int(x) for x in input().split()])


ans = 0
for line in grid:
	for i in range(11):
		chunk = line[i:i+5]
		if chunk == [1]*5 or chunk == [2]*5:
			ans = max(chunk)

for i in range(15):
	for j in range(11):
		chunk = [grid[j][i]]
		for m in range(1, 5):
			chunk.append(grid[j+m][i])
		if chunk == [1]*5 or chunk == [2]*5:
			ans = max(chunk)


for i in range(10, 0, -1):
	for j in range()

print(ans)