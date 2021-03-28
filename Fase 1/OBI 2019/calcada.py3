
N = int(input())
CAL = [0 for i in range(N)]
for i in range(N):
	CAL[i] = int(input())

ans = 0

for i in range(N):
	for j in range(i, N):
		a, b = CAL[i], CAL[j]

		last = -1
		resp_local = 0

		for k in range(N):
			c = CAL[k]
			if c != a and c != b or c == last:
				continue
			resp_local += 1
			last = c

		ans = max(ans, resp_local)

print(ans)