def permute(string, begin, end):
	if begin == end:
		lista.append(''.join(string))
	else:
		for i in range(begin, end+1):
			string[begin], string[i] = string[i], string[begin]
			print(f'{i} - {string} - Antes')
			permute(string, begin+1, end)
			string[begin], string[i] = string[i], string[begin]
			print(f'{i} - {string} - Backtracking\n\n')

lista = []
string = 'mateus'
a = permute(list(string), 0, len(string)-1)
print('\n'.join(lista))