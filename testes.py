T = int(input())

for _ in range(T):
	N = int(input())
	students = str(input()).split(' ')
	register = str(input()).split(' ')
	reproved = []

	for s, r in zip(students, register):
		doctor = r.count('M')
		freq = r.count('P') / (len(r) - doctor)

		if freq < 0.75:
			reproved.append(s)

	print(' '.join(reproved))