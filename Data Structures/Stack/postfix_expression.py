def postfix_expression(expression):
	stack = []

	for c in expression:
		if c.isdigit():
			stack.append(int(c))
		else:
			x = stack.pop()
			y = stack.pop()
			stack.append(int(eval(f'{y} {c} {x}')))
		print(stack)
	return stack.pop()



expression = '545*+5/'
expression = '138*+'
print(postfix_expression(expression))