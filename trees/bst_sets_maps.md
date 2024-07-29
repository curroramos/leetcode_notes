### Binary Search Tree (BST) Sets and Maps Overview
Binary Search Trees (BST) can be used to implement both sets and maps (dictionaries). A set is a collection of unique elements, while a map (or dictionary) is a collection of key-value pairs where each key is unique.

### BST Sets
A BST set maintains a collection of unique elements in a sorted order. The basic operations include insertion, deletion, and search, ensuring that all elements are unique and ordered.

#### Basic Operations for BST Sets

1. **Insertion:**
   - Add a new element to the set while maintaining the BST property. If the element already exists, it is not added again.

**Example Code for Insertion in BST Set:**
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTSet:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)
        # If value == node.value, do nothing (no duplicates allowed)

    def contains(self, value):
        return self._contains(self.root, value)

    def _contains(self, node, value):
        if node is None:
            return False
        if value < node.value:
            return self._contains(node.left, value)
        elif value > node.value:
            return self._contains(node.right, value)
        else:
            return True

    def in_order_traversal(self):
        elements = []
        self._in_order_traversal(self.root, elements)
        return elements

    def _in_order_traversal(self, node, elements):
        if node:
            self._in_order_traversal(node.left, elements)
            elements.append(node.value)
            self._in_order_traversal(node.right, elements)

# Example usage
bst_set = BSTSet()
bst_set.insert(10)
bst_set.insert(5)
bst_set.insert(15)
bst_set.insert(10)  # Duplicate, will not be added
print(bst_set.contains(10))  # Output: True
print(bst_set.contains(7))   # Output: False
print(bst_set.in_order_traversal())  # Output: [5, 10, 15]
```

2. **Deletion:**
   - Remove an element from the set while maintaining the BST property.

**Example Code for Deletion in BST Set:**
```python
def delete(self, value):
    self.root = self._delete(self.root, value)

def _delete(self, node, value):
    if node is None:
        return node
    if value < node.value:
        node.left = self._delete(node.left, value)
    elif value > node.value:
        node.right = self._delete(node.right, value)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        temp = self._find_min(node.right)
        node.value = temp.value
        node.right = self._delete(node.right, temp.value)
    return node

def _find_min(self, node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Example usage
bst_set.delete(10)
print(bst_set.in_order_traversal())  # Output: [5, 15]
```

### BST Maps (Dictionaries)
A BST map maintains a collection of key-value pairs where each key is unique and the keys are sorted. The basic operations include insertion, deletion, search, and retrieval of values.

#### Basic Operations for BST Maps

1. **Insertion:**
   - Add a new key-value pair to the map while maintaining the BST property. If the key already exists, update its value.

**Example Code for Insertion in BST Map:**
```python
class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BSTMap:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key, value)
            else:
                self._insert(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key, value)
            else:
                self._insert(node.right, key, value)
        else:
            node.value = value  # Update the value if key already exists

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.value

    def contains(self, key):
        return self._contains(self.root, key)

    def _contains(self, node, key):
        if node is None:
            return False
        if key < node.key:
            return self._contains(node.left, key)
        elif key > node.key:
            return self._contains(node.right, key)
        else:
            return True

    def in_order_traversal(self):
        elements = []
        self._in_order_traversal(self.root, elements)
        return elements

    def _in_order_traversal(self, node, elements):
        if node:
            self._in_order_traversal(node.left, elements)
            elements.append((node.key, node.value))
            self._in_order_traversal(node.right, elements)

# Example usage
bst_map = BSTMap()
bst_map.insert(10, "ten")
bst_map.insert(5, "five")
bst_map.insert(15, "fifteen")
bst_map.insert(10, "TEN")  # Update value for key 10
print(bst_map.get(10))  # Output: TEN
print(bst_map.get(7))   # Output: None
print(bst_map.in_order_traversal())  # Output: [(5, 'five'), (10, 'TEN'), (15, 'fifteen')]
```

2. **Deletion:**
   - Remove a key-value pair from the map while maintaining the BST property.

**Example Code for Deletion in BST Map:**
```python
def delete(self, key):
    self.root = self._delete(self.root, key)

def _delete(self, node, key):
    if node is None:
        return node
    if key < node.key:
        node.left = self._delete(node.left, key)
    elif key > node.key:
        node.right = self._delete(node.right, key)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        temp = self._find_min(node.right)
        node.key, node.value = temp.key, temp.value
        node.right = self._delete(node.right, temp.key)
    return node

def _find_min(self, node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Example usage
bst_map.delete(10)
print(bst_map.in_order_traversal())  # Output: [(5, 'five'), (15, 'fifteen')]
```

### Applications of BST Sets and Maps
- **Efficient Searching:** Quickly find elements or key-value pairs.
- **Range Queries:** Retrieve all elements or key-value pairs within a certain range.
- **Order Statistics:** Find the k-th smallest or largest element.
- **Dictionaries and Symbol Tables:** Implement dictionaries and symbol tables for efficient data retrieval.

### Advantages and Disadvantages
**Advantages:**
- **Efficient Operations:** Average-case time complexity of O(log n) for insertion, deletion, and search.
- **Sorted Order:** Maintains elements in sorted order, which is useful for range queries and ordered traversal.

**Disadvantages:**
- **Unbalanced Trees:** In the worst case, the time complexity can degrade to O(n) if the tree becomes unbalanced.
- **Space Overhead:** Requires additional space for storing pointers.

### Balanced BST Implementations
To overcome the disadvantages of unbalanced BSTs, balanced BSTs like AVL trees and Red-Black trees are used, ensuring O(log n) time complexity for operations.
