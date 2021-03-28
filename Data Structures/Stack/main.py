from stack import Stack 

stk = Stack()

# Appending elements
a = stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)

# Print the stack
stk.print_stack()

# Top of the stack
print('Top:', stk.top())

# Verifying if the stack is empty
print(stk.empty())

# Removing elements
a = stk.pop()
stk.pop()
stk.pop()
stk.pop()


# Verifying if the stack is empty
print(stk.empty())

