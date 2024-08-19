### Binary Trees Overview
A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child. Binary trees are used in various applications, including expression parsing, searching, and sorting.

### Key Concepts
1. **Node:** The basic unit of a binary tree containing data and references to its children.
2. **Root:** The topmost node of the tree.
3. **Leaf:** A node with no children.
4. **Internal Node:** A node with at least one child.
5. **Height:** The length of the longest path from the root to a leaf.
6. **Depth:** The length of the path from the root to a specific node.

### Types of Binary Trees
1. **Full Binary Tree:** Every node has either 0 or 2 children.
2. **Complete Binary Tree:** All levels are completely filled except possibly the last level, which is filled from left to right.
3. **Perfect Binary Tree:** All internal nodes have exactly two children and all leaf nodes are at the same level.
4. **Balanced Binary Tree:** The height of the left and right subtrees of any node differ by at most one.
5. **Binary Search Tree (BST):** A binary tree where for each node, the value of all nodes in the left subtree is less, and the value of all nodes in the right subtree is greater.

### Basic Operations
1. **Insertion:**
   - Add a new node in a binary search tree while maintaining the BST property.

**Example Code for Insertion in BST:**
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# Example usage
root = TreeNode(10)
insert(root, 5)
insert(root, 15)
insert(root, 2)
insert(root, 7)
```

2. **Deletion:**
   - Remove a node from a BST while maintaining the BST property.
   - Three cases:
     1. Node is a leaf (no children).
     2. Node has one child.
     3. Node has two children.

**Example Code for Deletion in BST:**
```python
def delete_node(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = delete_node(root.left, value)
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)
    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Example usage
delete_node(root, 5)
```

3. **Search:**
   - Find a node with a given value in a BST.

**Example Code for Search in BST:**
```python
def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)

# Example usage
node = search(root, 7)
```

4. **Traversal:**
   - Visit all nodes in a specific order.
   - Types of traversal:
     - **In-order:** Left, Root, Right
     - **Pre-order:** Root, Left, Right
     - **Post-order:** Left, Right, Root
     - **Level-order (Breadth-First):** Visit nodes level by level.

**Example Code for Tree Traversals:**
```python
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=' ')
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root:
        print(root.value, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=' ')

def level_order_traversal(root):
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
in_order_traversal(root)
print()
pre_order_traversal(root)
print()
post_order_traversal(root)
print()
level_order_traversal(root)
print()
```

### Applications of Binary Trees
- **Binary Search Trees:** Efficient searching, insertion, and deletion.
- **Heap Trees:** Implement priority queues.
- **Syntax Trees:** Used in compilers to parse expressions.
- **Huffman Coding Trees:** Used in data compression algorithms.
- **Trie:** Used for efficient retrieval of a key in a dataset of strings.

### Balanced Binary Trees
Balanced binary trees ensure that the height of the tree is logarithmic in terms of the number of nodes, which guarantees O(log n) time complexity for insertion, deletion, and search operations. Examples include AVL trees and Red-Black trees.

### Example of an AVL Tree (Self-Balancing Binary Search Tree)
**Insertion and Rotation:**
```python
class AVLTreeNode(TreeNode):
    def __init__(self, value):
        super().__init__(value)
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = max(get_height(z.left), get_height(z.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    return y

def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = max(get_height(z.left), get_height(z.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    return y

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def avl_insert(root, value):
    if not root:
        return AVLTreeNode(value)
    if value < root.value:
        root.left = avl_insert(root.left, value)
    else:
        root.right = avl_insert(root.right, value)

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1 and value < root.left.value:
        return right_rotate(root)
    if balance < -1 and value > root.right.value:
        return left_rotate(root)
    if balance > 1 and value > root.left.value:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and value < root.right.value:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Example usage
avl_root = None
avl_root = avl_insert(avl_root, 10)
avl_root = avl_insert(avl_root, 20)
avl_root = avl_insert(avl_root, 30)
avl_root = avl_insert(avl_root, 40)
avl_root = avl_insert(avl_root, 50)
avl_root = avl_insert(avl_root, 25)
```
