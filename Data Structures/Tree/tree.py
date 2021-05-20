
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def find_sum(root):
	if root == None:
		return 0

	global nodes
	nodes += 1

	return root.data + find_sum(root.left) + find_sum(root.right)


nodes = 0

root = Node(2)
root.left = Node(3)
root.right = Node(4)

a = root.right
b = root.left

a.right = Node(6)
b.left = Node(5)

tree_sum = find_sum(root)

print(f'The sum of the {nodes} nodes of this tree is: {tree_sum}')
