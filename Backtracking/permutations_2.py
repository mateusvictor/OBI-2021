def permute(string, length):
	if length == 1:
		return string
	else:
		ans = []
		for x in permute(string, length-1):
			for y in permute(string, 1):
				ans.append(y+x)
		return ans


string = list('abc')
print(permute(string, len(string)))