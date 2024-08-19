### Binary Search Trees (BST) Overview
A Binary Search Tree (BST) is a binary tree with the following properties:
1. **Left Subtree:** The left subtree of a node contains only nodes with keys less than the node’s key.
2. **Right Subtree:** The right subtree of a node contains only nodes with keys greater than the node’s key.
3. **No Duplicates:** There are no duplicate nodes.

### Key Concepts
- **Node:** Each element in the BST.
- **Root:** The top node of the BST.
- **Leaf:** A node with no children.
- **Internal Node:** A node with at least one child.
- **Height:** The length of the longest path from the root to a leaf.
- **Depth:** The length of the path from the root to a specific node.

### Basic Operations
1. **Insertion:**
   - Insert a new node into the BST while maintaining the BST property.

**Example Code for Insertion:**
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
   - Remove a node from the BST while maintaining the BST property.
   - Three cases:
     1. Node is a leaf (no children).
     2. Node has one child.
     3. Node has two children.

**Example Code for Deletion:**
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
   - Find a node with a given value in the BST.

**Example Code for Search:**
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

### Properties of Binary Search Trees
- **Time Complexity:**
  - Average Case: O(log n) for insertion, deletion, and search.
  - Worst Case: O(n) for insertion, deletion, and search (occurs when the tree becomes unbalanced and resembles a linked list).
- **Space Complexity:** O(n) for storing n nodes.

### Balanced Binary Search Trees
To ensure that the tree remains balanced and maintains O(log n) time complexity, self-balancing BSTs are used:
1. **AVL Trees:**
   - Height-balanced trees where the difference in height between left and right subtrees is at most one.
   - Requires rotations to maintain balance after insertions and deletions.

**Example of AVL Tree Insertion with Rotations:**
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

2. **Red-Black Trees:**
   - A type of self-balancing BST where each node has an extra bit for denoting the color of the node (red or black).
   - Ensures balance through specific properties and rotations.

### Applications of Binary Search Trees
- **Searching and Retrieval:** Efficiently search for elements.
- **Dynamic Sets:** Support dynamic data sets with insertions and deletions.
- **In-Order Traversal:** Retrieve elements in sorted order.
- **Implementation of Abstract Data Types:** Such as sets, multisets, and associative arrays.

These notes cover the key concepts, operations, and types of binary search trees. Let me know if you need more details or have any specific questions!