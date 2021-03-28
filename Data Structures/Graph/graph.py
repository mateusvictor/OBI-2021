# A class implementation of a graph (adjacency list)
# Undirected graph
from queue import Queue
class Graph:
	def __init__(self):
		self.graph_dict = {}
		self.shortest_path_to_root = []

	def add_edge(self, start, end):
		if start in self.graph_dict:
			self.graph_dict[start].append(end)
		else:
			self.graph_dict[start] = [end]

	def vertices(self):
		return len(self.graph_dict)

	def to_dict(self):
		return self.graph_dict

	def print_graph(self):
		for node, chields in self.graph_dict.items():
			print(f'{node} -> {chields}')

	def get_paths(self, start, end, path=[]):
		path = path + [start]

		if start == end:
			return [path]

		if start not in self.graph_dict:
			return []

		paths = []

		for node in self.graph_dict[start]:
			if node not in path:
				new_paths = self.get_paths(node, end, path)
				paths+=new_paths

		return paths

	def get_shortest_path(self, start, end, path=[]):
		path = path + [start]

		if start == end:
			return path

		if start not in self.graph_dict:
			return None

		shortest_path = None

		for node in self.graph_dict[start]:
			if node not in path:
				sp = self.get_shortest_path(node, end, path)
				if sp:
					if shortest_path is None or len(sp) < len(shortest_path):
						shortest_path = sp

		return shortest_path

	def bfs(self, start, end):
		visited = {node:False for node in self.graph_dict.keys()}
		level = {node:-1 for node in self.graph_dict.keys()}
		parent = {node:None for node in self.graph_dict.keys()}
		bfs_traversal_output = []
		queue = Queue()

		visited[start] = True
		level[start] = 0

		queue.put(start)

		while not queue.empty():
			u = queue.get()
			bfs_traversal_output.append(u)

			for vertex in self.graph_dict[u]:
				if not visited[vertex]:
					visited[vertex] = True
					parent[vertex] = u
					level[vertex] = level[u]+1
					queue.put(vertex)
		'''

		v = 2
		self.shortest_path_to_root = []
		while v is not None:
			self.shortest_path_to_root.append(v)
			v = parent[v]
		self.shortest_path_to_root.reverse()
		print(self.shortest_path_to_root)
		'''
		return bfs_traversal_output
