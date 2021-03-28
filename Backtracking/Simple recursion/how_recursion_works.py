def print_function(test):
	if test < 1:
		return
	else:
		print(test, end=' ')
		print_function(test-1)
		print(test, end=' ')
		return

print(print_function(3))