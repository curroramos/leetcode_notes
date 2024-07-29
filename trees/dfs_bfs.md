### Depth-First Search (DFS) and Breadth-First Search (BFS) Overview
Depth-First Search (DFS) and Breadth-First Search (BFS) are two fundamental algorithms for traversing or searching tree and graph data structures.

### Depth-First Search (DFS)
DFS explores a tree (or graph) by starting at the root (or an arbitrary node) and explores as far as possible along each branch before backtracking. There are three common ways to implement DFS in trees: in-order, pre-order, and post-order traversal.

#### DFS Implementations

1. **In-Order Traversal (Left, Root, Right):**
   - Visit the left subtree.
   - Visit the root node.
   - Visit the right subtree.

**Example Code:**
```python
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=' ')
        in_order_traversal(root.right)

# Example usage
in_order_traversal(root)
```

2. **Pre-Order Traversal (Root, Left, Right):**
   - Visit the root node.
   - Visit the left subtree.
   - Visit the right subtree.

**Example Code:**
```python
def pre_order_traversal(root):
    if root:
        print(root.value, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

# Example usage
pre_order_traversal(root)
```

3. **Post-Order Traversal (Left, Right, Root):**
   - Visit the left subtree.
   - Visit the right subtree.
   - Visit the root node.

**Example Code:**
```python
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=' ')

# Example usage
post_order_traversal(root)
```

### Breadth-First Search (BFS)
BFS explores a tree (or graph) level by level, starting from the root and moving to the next level, visiting all nodes at the current level before moving to the next level. BFS is typically implemented using a queue.

**Example Code:**
```python
def bfs(root):
    if root is None:
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.value, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# Example usage
bfs(root)
```

### Applications of DFS and BFS in Trees

#### Depth-First Search (DFS)
- **In-Order Traversal:** Used for retrieving the elements of a binary search tree in sorted order.
- **Pre-Order Traversal:** Used to create a copy of the tree or to get a prefix expression of an expression tree.
- **Post-Order Traversal:** Used to delete the tree or to get a postfix expression of an expression tree.

#### Breadth-First Search (BFS)
- **Level-Order Traversal:** Used to find the shortest path in an unweighted tree or graph.
- **Finding the Minimum Depth:** BFS is used to find the minimum depth of a binary tree.
- **Serialization and Deserialization:** BFS is often used for serializing and deserializing binary trees.

### Example Usage and Practical Problems

1. **Find the Maximum Depth of a Binary Tree Using DFS:**
```python
def max_depth(root):
    if root is None:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1

# Example usage
depth = max_depth(root)
print(depth)
```

2. **Find the Minimum Depth of a Binary Tree Using BFS:**
```python
def min_depth(root):
    if root is None:
        return 0
    queue = [(root, 1)]
    while queue:
        current, depth = queue.pop(0)
        if current.left is None and current.right is None:
            return depth
        if current.left:
            queue.append((current.left, depth + 1))
        if current.right:
            queue.append((current.right, depth + 1))

# Example usage
depth = min_depth(root)
print(depth)
```

3. **Check if a Binary Tree is Symmetric Using DFS:**
```python
def is_symmetric(root):
    def is_mirror(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.value == t2.value) and is_mirror(t1.right, t2.left) and is_mirror(t1.left, t2.right)

    return is_mirror(root, root)

# Example usage
print(is_symmetric(root))
```

4. **Level Order Traversal Using BFS:**
```python
def level_order_traversal(root):
    if root is None:
        return []
    result, queue = [], [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

# Example usage
levels = level_order_traversal(root)
for level in levels:
    print(level)
```
