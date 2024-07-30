### Graphs Overview

A graph is a data structure that consists of a set of nodes (or vertices) and a set of edges connecting the nodes. Graphs are used to model relationships between objects and are widely used in various fields such as computer science, mathematics, social sciences, and more.

### Types of Graphs

1. **Directed Graph (Digraph):** A graph where the edges have a direction, indicating the relationship flows from one vertex to another.
2. **Undirected Graph:** A graph where the edges have no direction, indicating a mutual relationship between the vertices.
3. **Weighted Graph:** A graph where edges have weights or costs associated with them.
4. **Unweighted Graph:** A graph where edges do not have any weights or costs.
5. **Cyclic Graph:** A graph that contains at least one cycle, a path that starts and ends at the same vertex.
6. **Acyclic Graph:** A graph that does not contain any cycles.

### Graph Representation

1. **Adjacency Matrix:**
   - A 2D array where the element at row \(i\) and column \(j\) indicates whether there is an edge from vertex \(i\) to vertex \(j\).
   
   **Example Code:**
   ```python
   class GraphMatrix:
       def __init__(self, num_vertices):
           self.num_vertices = num_vertices
           self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

       def add_edge(self, u, v, weight=1):
           self.matrix[u][v] = weight
           # For undirected graph, add the reverse edge
           # self.matrix[v][u] = weight

       def remove_edge(self, u, v):
           self.matrix[u][v] = 0
           # For undirected graph, remove the reverse edge
           # self.matrix[v][u] = 0

       def display(self):
           for row in self.matrix:
               print(row)

   # Example usage
   graph_matrix = GraphMatrix(5)
   graph_matrix.add_edge(0, 1)
   graph_matrix.add_edge(0, 4)
   graph_matrix.add_edge(1, 2)
   graph_matrix.add_edge(1, 3)
   graph_matrix.add_edge(1, 4)
   graph_matrix.add_edge(2, 3)
   graph_matrix.add_edge(3, 4)
   graph_matrix.display()
   ```

2. **Adjacency List:**
   - An array of lists where the \(i\)-th list contains the vertices adjacent to the \(i\)-th vertex.
   
   **Example Code:**
   ```python
   class GraphList:
       def __init__(self, num_vertices):
           self.num_vertices = num_vertices
           self.adj_list = [[] for _ in range(num_vertices)]

       def add_edge(self, u, v):
           self.adj_list[u].append(v)
           # For undirected graph, add the reverse edge
           # self.adj_list[v].append(u)

       def remove_edge(self, u, v):
           self.adj_list[u].remove(v)
           # For undirected graph, remove the reverse edge
           # self.adj_list[v].remove(u)

       def display(self):
           for i in range(self.num_vertices):
               print(f"Vertex {i}: {self.adj_list[i]}")

   # Example usage
   graph_list = GraphList(5)
   graph_list.add_edge(0, 1)
   graph_list.add_edge(0, 4)
   graph_list.add_edge(1, 2)
   graph_list.add_edge(1, 3)
   graph_list.add_edge(1, 4)
   graph_list.add_edge(2, 3)
   graph_list.add_edge(3, 4)
   graph_list.display()
   ```

### Graph Traversal

1. **Depth-First Search (DFS):**
   - A traversal method that explores as far as possible along each branch before backtracking.
   
   **Example Code:**
   ```python
   def dfs(graph, start):
       visited = set()
       stack = [start]
       while stack:
           vertex = stack.pop()
           if vertex not in visited:
               visited.add(vertex)
               print(vertex, end=' ')
               for neighbor in reversed(graph[vertex]):
                   stack.append(neighbor)

   # Example usage
   graph = {
       0: [1, 4],
       1: [0, 2, 3, 4],
       2: [1, 3],
       3: [1, 2, 4],
       4: [0, 1, 3]
   }
   dfs(graph, 0)
   ```

2. **Breadth-First Search (BFS):**
   - A traversal method that explores all the vertices at the present depth level before moving on to the vertices at the next depth level.
   
   **Example Code:**
   ```python
   def bfs(graph, start):
       visited = set()
       queue = [start]
       while queue:
           vertex = queue.pop(0)
           if vertex not in visited:
               visited.add(vertex)
               print(vertex, end=' ')
               for neighbor in graph[vertex]:
                   if neighbor not in visited:
                       queue.append(neighbor)

   # Example usage
   graph = {
       0: [1, 4],
       1: [0, 2, 3, 4],
       2: [1, 3],
       3: [1, 2, 4],
       4: [0, 1, 3]
   }
   bfs(graph, 0)
   ```

### Applications of Graphs

1. **Social Networks:** Model relationships between individuals.
2. **Web Crawling:** Represent web pages and links.
3. **Routing Algorithms:** Find the shortest path in networks.
4. **Dependency Resolution:** Task scheduling and project planning.
5. **Recommendation Systems:** Model user-item relationships.

### Advanced Graph Algorithms

1. **Dijkstra's Algorithm:**
   - Finds the shortest path from a single source to all other vertices in a weighted graph.
   
   **Example Code:**
   ```python
   import heapq

   def dijkstra(graph, start):
       min_heap = [(0, start)]
       distances = {vertex: float('infinity') for vertex in graph}
       distances[start] = 0

       while min_heap:
           current_distance, current_vertex = heapq.heappop(min_heap)

           if current_distance > distances[current_vertex]:
               continue

           for neighbor, weight in graph[current_vertex].items():
               distance = current_distance + weight
               if distance < distances[neighbor]:
                   distances[neighbor] = distance
                   heapq.heappush(min_heap, (distance, neighbor))

       return distances

   # Example usage
   graph = {
       'A': {'B': 1, 'C': 4},
       'B': {'A': 1, 'C': 2, 'D': 5},
       'C': {'A': 4, 'B': 2, 'D': 1},
       'D': {'B': 5, 'C': 1}
   }
   print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
   ```

2. **Kruskal's Algorithm:**
   - Finds the Minimum Spanning Tree (MST) for a weighted graph.
   
   **Example Code:**
   ```python
   class DisjointSet:
       def __init__(self, vertices):
           self.parent = {v: v for v in vertices}
           self.rank = {v: 0 for v in vertices}

       def find(self, item):
           if self.parent[item] == item:
               return item
           else:
               self.parent[item] = self.find(self.parent[item])
               return self.parent[item]

       def union(self, set1, set2):
           root1 = self.find(set1)
           root2 = self.find(set2)

           if root1 != root2:
               if self.rank[root1] > self.rank[root2]:
                   self.parent[root2] = root1
               else:
                   self.parent[root1] = root2
                   if self.rank[root1] == self.rank[root2]:
                       self.rank[root2] += 1

   def kruskal(graph):
       edges = []
       for vertex in graph:
           for neighbor, weight in graph[vertex].items():
               edges.append((weight, vertex, neighbor))
       edges.sort()

       ds = DisjointSet(graph.keys())
       mst = []

       for edge in edges:
           weight, u, v = edge
           if ds.find(u) != ds.find(v):
               ds.union(u, v)
               mst.append((u, v, weight))

       return mst

   # Example usage
   graph = {
       'A': {'B': 1, 'C': 4},
       'B': {'A': 1, 'C': 2, 'D': 5},
       'C': {'A': 4, 'B': 2, 'D': 1},
       'D': {'B': 5, 'C': 1}
   }
   print(kruskal(graph))  # Output: [('A', 'B', 1), ('C', 'D', 1), ('B', 'C', 2)]
   ```

3. **Topological Sort:**
   - Orders vertices in a directed acyclic graph (DAG) such that for every directed

 edge \(uv\), vertex \(u\) comes before \(v\) in the ordering.
   
   **Example Code:**
   ```python
   def topological_sort(graph):
       def dfs(vertex):
           visited.add(vertex)
           for neighbor in graph[vertex]:
               if neighbor not in visited:
                   dfs(neighbor)
           stack.append(vertex)

       visited = set()
       stack = []

       for vertex in graph:
           if vertex not in visited:
               dfs(vertex)

       return stack[::-1]

   # Example usage
   graph = {
       'A': ['B', 'C'],
       'B': ['D'],
       'C': ['D'],
       'D': []
   }
   print(topological_sort(graph))  # Output: ['A', 'C', 'B', 'D']
   ```

### Advantages and Disadvantages

**Advantages:**
- **Model Complex Relationships:** Can represent various types of relationships and connections.
- **Efficient Algorithms:** Many efficient algorithms exist for searching, pathfinding, and optimization.

**Disadvantages:**
- **Memory Usage:** Can use significant memory for storing vertices and edges.
- **Complexity:** Some graph algorithms can be complex and computationally expensive for large graphs.

These notes cover the key concepts, implementations, and applications of graphs. Let me know if you need more details or have any specific questions!