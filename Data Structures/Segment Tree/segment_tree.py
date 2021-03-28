# https://noic.com.br/informatica/curso-noic/data-structures-09/

def build(node, start, end):
	if start == end:
		tree[node] = vet[start]
		return

	mid = int((start+end) / 2)

	build(2*node + 1, 1, mid)
	build(2*node + 2, mid+1, end)

	tree[node] = tree[2*node + 1] + tree[2*node + 2]


def update(node, start, end, idx, x):
	if start == end:
		tree[node] = x
		vet[start] = x
		return

	mid = int((start+end) / 2)

	if start <= idx and idx <= mid:
		update(2*node + 1, start, mid, idx, x)
	else:
		update(2*node + 2, mid+1, end, idx, x)

	tree[node] = tree[2*node + 1] + tree[2*node + 2]



vet = [1, 2, 4, 3, 5, 10]
tree = [25, 7, 18, 3, 4, 8, 10, 1, 2, None, None, 3, 5, None, None]
# Representing in a segment tree
# tree[2*i + 1] -> left child
# tree[2*i + 2] -> right child
