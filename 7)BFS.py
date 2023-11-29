from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current_vertex = queue.popleft()
        print(current_vertex, end=' ')

        for neighbor in graph.get(current_vertex, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

my_graph = Graph()
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 4)
my_graph.add_edge(2, 5)
my_graph.add_edge(3, 6)

print("Breadth-First Search:")
bfs(my_graph.graph, 1)
