N = int(input())

prices = sorted([int(input()) for _ in range(N)], reverse=True)
groups = [prices[i:i+3] for i in range(0, N, 3)]

topay = 0
for group in groups:
	if len(group) != 3:
		topay += sum(group)
	else:
		topay += sum(group) - min(group)

print(topay)