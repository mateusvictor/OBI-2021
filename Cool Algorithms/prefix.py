n, k = [int(x) for x in input().split()]
array = [int(x) for x in input().split()]
table = {0:1}

soma = 0
result = 0

for n in array:
	soma += n
	if soma-k in table:
		result += table[soma-k]

	table[soma] = table.get(soma, 0) + 1
	print(table, result)

print(result)