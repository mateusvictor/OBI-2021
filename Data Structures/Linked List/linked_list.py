# Class implementation of linked list

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):
		temp = self.head

		while temp:
			print(temp.data)
			temp = temp.next

	def push_front(self, new_data):
		# Function to insert a new node at the beginning

		# Step 1 and 2: create the node and put in the data
		new_node = Node(new_data)

		# Step 3: make next of new node as head
		new_node.next = self.head

		# Step 4: move the head to point to the new node
		self.head = new_node

	def insert(self, prev_node, new_data):
		# Function to insert a new node between 2 existent nodes
		
		# Step 1: check if the given prev_node exists
		if prev_node is None:
			print("ERRO: The fiven previous node must exists in the liked list.")
			return 

		# Step 2 and 3: create a node and put in the data
		new_node = Node(new_data)

		# Step 4: make next of new node as next of the prev node
		new_node.next = prev_node.next

		# Step 5: make next of prev_node as new_node
		prev_node.next = new_node

	def push_back(self, new_data):
		# Function to insert a new node at the end of the linked list

		# Step 1 and 2: create a node and and put in the data
		new_node = Node(new_data)

		# Step 3: if the linked list is empty, make the new node as head
		if self.head is None:
			self.head = new_node
			return 

		# Step 4: iterate till find the last node
		last = self.head
		while last.next:
			last = last.next

		last.next = new_node

	def delete_node(self, value):
		# Delete the node with the first occurence of the value

		temp = self.head

		# If head node itself holds the value to be deleted
		if temp is not None and temp.data == value:
			self.head = temp.next
			temp = None
			return 

		# Search for the value to be deleted 
		while temp != None:
			if temp.data == value:
				break
			prev = temp
			temp = temp.next

		if temp == None:
			return -1

		prev.next = temp.next
		temp = None

	def delete(self):
		current = self.head
		while current:
			temp = current.next

			del current.data
			current = temp

	def length(self):
		counter = 0
		current = self.head

		while current:
			counter += 1
			current = current.next

		return counter

	def search(self, value):
		current = self.head

		while current != None:
			if current.data == value:
				return True

			current = current.next

		return False

	def index(self, index):
		current = self.head
		counter = 0

		while current:
			if counter == index:
				return current.data

			counter += 1
			current = current.next

		return False