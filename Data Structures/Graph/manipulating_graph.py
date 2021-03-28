#from graph import AdjNode, Graph
from graph import Graph


graph = Graph()

routes = [
	("Mumbai", "Paris"),
	("Mumbai", "Dubai"),
	("Paris", "Dubai"),
	("Paris", "New York"),
	("Dubai", "New York")
]

routes = [
	(0, 1), (0, 4), (1, 0), (1, 4), (1, 2),
	(1, 3), (2, 1), (2, 3), (3, 1), (3, 4),
	(3, 2), (4, 3), (4, 0), (4, 1,),
]

for route in routes:
	graph.add_edge(route[0], route[1])

graph.print_graph()
#print(graph.to_dict())


start = 0
end = 2
print(graph.bfs(start, end))


paths =  graph.get_paths(start, end)
print(f"\n\nPaths between {start} and {end}: ")

for path in paths:
	print(f"\t{' -> '.join(map(str, path))}")


sp = graph.get_shortest_path(start, end)
print("\nShortest path between {start} and {end}:")
print(f"\t{' -> '.join(map(str, sp))}")
