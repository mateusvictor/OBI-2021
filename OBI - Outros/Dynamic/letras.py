# https://olimpiada.ic.unicamp.br/pratique/p1/2015/f2/letras/

def LIS():
	lis = [1] * len(word)

	for i in range(1, len(lis)):
		subproblems = [lis[k] for k in range(i) if word[k] <= word[i]]
		lis[i] = 1 + max(subproblems, default=0)

	return max(lis)


word = list(input())

for i in range(len(word)):
	word[i] = ord(word[i]) - 64

print(LIS())