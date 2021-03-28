from linked_list import Node, LinkedList

llist = LinkedList()
llist.push_back(1)
llist.push_back(2)
llist.push_back(3)
llist.push_back(4)
llist.push_back(5)

print('Linked list created:')
llist.print_list()

value = 5
index = 3

if llist.search(value=value):
	print(f'Value {value} found!')
else:
	print(f'Value {value} was not found')

print(f'Index: {index} => Value: {llist.index(index=index)}')