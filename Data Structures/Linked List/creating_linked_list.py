from linked_list import Node, LinkedList


llist = LinkedList()
llist.head = Node(1)

second = Node(2)
llist.head.next = second

third = Node(3)
second.next = third

llist.print_list()
'''

llist.head        second              third 
     |                |                  | 
     |                |                  | 
+----+------+     +----+------+     +----+------+ 
| 1  |  o-------->| 2  |  o-------->|  3 | None | 
+----+------+     +----+------+     +----+------+  
'''
