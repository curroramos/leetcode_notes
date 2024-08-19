### Heap and Priority Queue Overview

A heap is a specialized tree-based data structure that satisfies the heap property. In a max heap, for any given node \(i\), the value of \(i\) is greater than or equal to the values of its children, and the highest value is at the root. In a min heap, for any given node \(i\), the value of \(i\) is less than or equal to the values of its children, and the lowest value is at the root.

A priority queue is an abstract data type similar to a regular queue or stack data structure, but where each element has a "priority" associated with it. In a priority queue, an element with high priority is served before an element with low priority. Heaps are commonly used to implement priority queues.

### Types of Heaps
1. **Max Heap:** The value of each node is greater than or equal to the values of its children.
2. **Min Heap:** The value of each node is less than or equal to the values of its children.

### Operations in Heaps

1. **Insertion:** Add a new element to the heap while maintaining the heap property.
2. **Deletion:** Remove the root element (the maximum in a max heap or the minimum in a min heap) while maintaining the heap property.
3. **Peek/Top:** Get the root element without removing it.
4. **Heapify:** Rearrange the elements to maintain the heap property.

### Implementing a Heap

#### Max Heap
**Example Code:**
```python
class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index != 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def get_max(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

# Example usage
max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(10)
max_heap.insert(5)
print(max_heap.get_max())  # Output: 10
print(max_heap.extract_max())  # Output: 10
print(max_heap.get_max())  # Output: 5
```

#### Min Heap
**Example Code:**
```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def get_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

# Example usage
min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(10)
min_heap.insert(5)
print(min_heap.get_min())  # Output: 3
print(min_heap.extract_min())  # Output: 3
print(min_heap.get_min())  # Output: 5
```

### Priority Queue using Heap

A priority queue can be implemented using a heap, with elements having a priority value. The heap operations ensure that the element with the highest (or lowest, depending on the heap type) priority is always at the root.

#### Example Priority Queue using Min Heap
**Example Code:**
```python
class PriorityQueue:
    def __init__(self):
        self.min_heap = MinHeap()

    def enqueue(self, item, priority):
        self.min_heap.insert((priority, item))

    def dequeue(self):
        if len(self.min_heap.heap) == 0:
            return None
        return self.min_heap.extract_min()[1]

    def peek(self):
        if len(self.min_heap.heap) == 0:
            return None
        return self.min_heap.get_min()[1]

# Example usage
pq = PriorityQueue()
pq.enqueue("task1", 3)
pq.enqueue("task2", 1)
pq.enqueue("task3", 2)
print(pq.peek())  # Output: task2
print(pq.dequeue())  # Output: task2
print(pq.peek())  # Output: task3
```

### Applications of Heaps and Priority Queues
1. **Priority Scheduling:** Managing tasks based on their priorities.
2. **Dijkstra's Algorithm:** Finding the shortest path in a graph.
3. **Heapsort:** A comparison-based sorting algorithm that uses a heap to sort elements.
4. **Merging K Sorted Lists:** Efficiently merge multiple sorted lists.

### Advantages and Disadvantages

**Advantages:**
- **Efficient Operations:** Heaps provide efficient insertion, deletion, and retrieval of the maximum or minimum element.
- **Dynamic:** Heaps can dynamically adjust as elements are added or removed, making them suitable for priority queues.

**Disadvantages:**
- **Not Ordered:** Unlike balanced search trees, heaps do not provide ordered traversal of elements.
- **Fixed Shape:** The tree shape is determined by the insertion order and the heap properties, which can limit flexibility in some use cases.

These notes cover the key concepts, implementations, and applications of heaps and priority queues. Let me know if you need more details or have any specific questions!