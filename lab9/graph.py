from collections import deque
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

#Implement Depth-First Search
    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

#Implement Breadth-First Search
    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

#Implement Method to Find All Paths
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

#Implement Meathod to check if Graph Connected
    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)

# Test the Graph class
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()
# Test DFS
print("\nDFS starting from vertex 0:")
g.dfs(0)
# Test BFS
print("\n\nBFS starting from vertex 0:")
g.bfs(0)
# Test Find All Paths
print("\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))
# Test if the graph is connected
print("\nIs the graph connected?", g.is_connected())
# Add a disconnected vertex and test again
g.add_vertex(4)
print("After adding a disconnected vertex:")
print("Is the graph connected?", g.is_connected())

#EXERCISE

#Implement a method to find the shortest path between two vertices
from collections import deque

def bfs_shortest_path(graph, start, goal):

    visited = set()

    queue = deque([[start]])
    
    while queue:
        path = queue.popleft()
        
        node = path[-1]
 
        if node == goal:
            return path

        elif node not in visited:
            visited.add(node)
            
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
  
    return None

# test
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
goal = 'F'
print(bfs_shortest_path(graph, start, goal)) 

#2.Add a method to detect cycles in the graph.
def detect_cycle_directed(graph):
    def dfs(node):
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    visited = set()
    visiting = set()

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

# Example usage
graph_directed = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['C'],
    'E': []
}

print(detect_cycle_directed(graph_directed))  

#3.Implement algorithm to find the shortest path in a weighted graph.

import heapq

def dijkstra(graph, start):
    
    priority_queue = [(0, start)]
    shortest_paths = {start: (None, 0)}
    
    while priority_queue:
        (current_distance, current_node) = heapq.heappop(priority_queue)
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if neighbor not in shortest_paths or distance < shortest_paths[neighbor][1]:
                shortest_paths[neighbor] = (current_node, distance)
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

def shortest_path(graph, start, end):
    paths = dijkstra(graph, start)
    route = []
    if end not in paths:
        return None
    
    while end is not None:
        route.append(end)
        next_node = paths[end][0]
        end = next_node
    
    route = route[::-1]
    return route, paths[route[-1]][1]

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start = 'A'
end = 'D'
path, distance = shortest_path(graph, start, end)
print(f"The shortest path from {start} to {end} is {path} with a total distance of {distance}.")

#4.Create a method to determine if the graph is bipartite.
from collections import deque

def is_bipartite(graph):
    color = {}
    
    for node in graph:
        if node not in color:
            queue = deque([node])
            color[node] = 0
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        return False
    return True

# test
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print(is_bipartite(graph))