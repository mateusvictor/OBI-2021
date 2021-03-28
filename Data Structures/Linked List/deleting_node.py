from linked_list import Node, LinkedList

llist = LinkedList()
llist.push_back(1)
llist.push_back(2)
llist.push_back(3)
llist.push_back(4)
llist.push_back(5)

print('Linked list created:')
llist.print_list()

value = 2

llist.delete_node(value=value)
print(f'\nLinked list after deletion of node with value {value}:')
llist.print_list()

print(f'\nLength: {llist.length()}')
llist.delete()