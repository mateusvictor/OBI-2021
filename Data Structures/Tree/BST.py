class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None


def bst_sum(root):
	if root is None:
		return 0

	return root.data + bst_sum(root.left) + bst_sum(root.right)


def binary_search(root, data):
	if root is None:
		return -1

	if root.data == data:
		return 'YEAAH'

	if data <= root.data:
		return binary_search(root.left, data)

	if data > root.data:
		return binary_search(root.right, data)


def insert(root, data):
	if root is None:
		return Node(data)

	if data <= root.data:
		root.left = insert(root.left, data)

	elif data > root.data:
		root.right = insert(root.right, data)


	return root 


def max_node(root):
	current = root

	while current.right:
		current = current.right

	return current.data


def min_node(root):
	current = root

	while current.left:
		current = current.left

	return current.data


def height(root):
	if root is None:
		return -1

	left_height = height(root.left)
	right_height = height(root.right)

	return max(left_height, right_height) + 1


root = Node(50)
values = [30, 20, 70, 60]

for v in values:
	node = insert(root, v)

print(bst_sum(root))
print(binary_search(root, 10))
print(max_node(root))
print(min_node(root))
print(height(root))