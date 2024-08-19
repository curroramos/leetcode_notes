### Breadth-First Search (BFS) in a Matrix

Breadth-First Search (BFS) is a fundamental algorithm for traversing or searching tree or graph data structures. When applied to a matrix, BFS can be used to explore all possible paths from a given starting point, find the shortest path, or explore all connected components in a grid.

### Key Concepts

1. **Queue:** BFS uses a queue data structure to keep track of the nodes to be explored next.
2. **Visited Array:** To keep track of visited nodes and avoid revisiting them.
3. **Directions Array:** To explore all possible directions (up, down, left, right) from a given cell.

### Example Problem: Finding the Shortest Path in a Binary Matrix

Given a binary matrix, find the shortest path from the top-left corner to the bottom-right corner. The path can only be constructed from cells with value 1, and you can only move up, down, left, or right.

### Example Code

```python
from collections import deque

def bfs_shortest_path(matrix):
    if not matrix or matrix[0][0] == 0 or matrix[-1][-1] == 0:
        return -1

    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = set((0, 0))

    while queue:
        r, c, dist = queue.popleft()

        # Check if we've reached the bottom-right corner
        if r == rows - 1 and c == cols - 1:
            return dist

        # Explore all possible directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == 1 and (nr, nc) not in visited:
                queue.append((nr, nc, dist + 1))
                visited.add((nr, nc))

    return -1  # No path found

# Example usage
matrix = [
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 1]
]

print(bfs_shortest_path(matrix))  # Output: 7
```

### Explanation

1. **Initialization:**
   - Check if the matrix is empty or if the starting or ending cell is blocked (contains 0). If so, return -1.
   - Initialize the `rows` and `cols` variables to store the dimensions of the matrix.
   - Define the possible directions for movement (up, down, left, right).
   - Initialize a queue with the starting cell (0, 0) and distance 1.
   - Create a `visited` set to keep track of visited cells and avoid revisiting them.

2. **BFS Loop:**
   - Dequeue a cell from the queue.
   - Check if the current cell is the bottom-right corner. If so, return the current distance as the shortest path length.
   - Explore all possible directions from the current cell.
   - For each direction, calculate the new row and column indices.
   - Check if the new indices are within bounds, the cell is not blocked (contains 1), and has not been visited.
   - If valid, enqueue the new cell with the incremented distance and mark it as visited.

3. **Termination:**
   - If the queue is empty and no path has been found, return -1.

### Variations and Applications

1. **Finding Connected Components:**
   - BFS can be used to find all connected components in a binary matrix (regions of 1s connected by edges).

2. **Shortest Path in Weighted Graphs:**
   - BFS can be adapted to find the shortest path in unweighted graphs or grids, while Dijkstra's algorithm is used for weighted graphs.

3. **Maze Solving:**
   - BFS is commonly used to solve maze problems, where the goal is to find the shortest path from the start to the end.

### Example: Finding All Connected Components in a Binary Matrix

```python
def bfs_connected_components(matrix):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    visited = set()

    def bfs(r, c):
        queue = deque([(r, c)])
        component = []
        while queue:
            cr, cc = queue.popleft()
            component.append((cr, cc))
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == 1 and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        return component

    components = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and (r, c) not in visited:
                visited.add((r, c))
                components.append(bfs(r, c))

    return components

# Example usage
matrix = [
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 0, 0, 0]
]

print(bfs_connected_components(matrix))
# Output: [[(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (2, 3), (1, 3), (0, 3)], [(3, 0)]]
```