class Employee:
	def __init__(self, age):
		self.age = age

def read_numbers():
	return [int(x) if x.isnumeric() else x for x in input().split()]

def youngest_manager(start):
	visited = {}
	youngest = '*'
	queue = [people[start]]

	while len(queue) > 0:
		actual = queue.pop(0)

		if visited.get(actual, False) or not graph.get(actual, False):
			continue

		visited[actual] = True

		for emp in graph[actual]:
			youngest = min(emp.age, youngest if youngest != '*' else float('inf'))
			queue.append(emp)

	return youngest

def dfs(start):
	visited[start] = True

	for vertex in graph[start]:
		if visited.get(vertex, False):
			continue
		youngest[0] = min(youngest[0], vertex.age)
		dfs(vertex)

def swap_employees(a, b):
	people[a].age, people[b].age, = people[b].age, people[a].age
	people[a], people[b] = people[b], people[a]

 
N, M, I = read_numbers()
people = [None] + read_numbers()
graph = {}

for i in range(1, N+1):
	people[i] = Employee(people[i])
	graph[people[i]] = []

for _ in range(M):
	A, B  = read_numbers()
	graph[people[B]].append(people[A])

for _ in range(I):
	inst = read_numbers()
	if inst[0] == 'P':
		visited = {}
		youngest = [float('inf')]
		dfs(people[inst[1]])
		print(youngest[0] if youngest[0] != float('inf') else '*')
	else:
		swap_employees(inst[1], inst[2])
