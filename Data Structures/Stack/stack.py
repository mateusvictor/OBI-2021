# Class implementation of a stack using lists
class Stack:
	def __init__(self):
		self.stack = []

	def empty(self):
		# Boolean to functoin 
		return True if not self.stack else False

	def push(self, item):
		# Function to add an item at the top of the stack
		self.stack.append(item)
		return item

	def pop(self):
		# Function to remove an item from stack
		if self.empty():
			return 
		
		return self.stack.pop()

	def top(self):
		# Function to return the top of the stack
		if self.empty():
			return

		return self.stack[-1]

	def print_stack(self):
		#
		if self.empty():
			return

		for i in range(len(self.stack) - 1, -1, -1):
			print(self.stack[i])