from linked_list import Node, LinkedList

# Creating a linked list
llist = LinkedList()

first = Node(0)
llist.head = first

second = Node(10)
first.next = second

third = Node(30)
second.next = third

print('Creating a linked list')
llist.print_list()

def main():
	# Inserting a node at the beginning of the linked list
	llist.push_front(new_data=-10)
	
	print('\nInserting a node at the beginning of the linked list')
	llist.print_list()

	# Inserting a node between two existent nodes
	llist.insert(prev_node=second, new_data=20)

	print('\nInserting a node between two existents elements')
	llist.print_list()

	# Inserting a node at the end of the linked list
	llist.push_back(new_data=40)

	print('\nInserting a node the end of the linked list')
	llist.print_list()

	# Print the length of a linked list
	print('Length of the linked list:', llist.length())

main()