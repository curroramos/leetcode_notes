### Queue Overview
A queue is a linear data structure that follows the First In First Out (FIFO) principle. The element that is added first will be removed first. 

### Basic Operations
1. **Enqueue:** Add an element to the end of the queue.
2. **Dequeue:** Remove an element from the front of the queue.
3. **Peek/Front:** Get the element at the front of the queue without removing it.
4. **IsEmpty:** Check if the queue is empty.
5. **Size:** Get the number of elements in the queue.

### Types of Queues
- **Simple Queue:** Also known as a linear queue. It follows the FIFO principle.
- **Circular Queue:** The last position is connected back to the first position to make a circle.
- **Priority Queue:** Every element is assigned a priority, and elements are dequeued based on their priority.
- **Double-ended Queue (Deque):** Insertion and deletion can be performed from both ends.

### Applications of Queues
- **CPU Scheduling:** Queues are used for managing tasks in a time-sharing system.
- **Breadth-First Search (BFS):** In graph traversal algorithms.
- **Asynchronous Data Transfer:** Queues are used in IO Buffers, pipes, file IO, etc.

### Implementation of a Simple Queue Using a List

**Enqueue Operation:**
- Append the element to the end of the list.
- Time Complexity: O(1)

**Dequeue Operation:**
- Remove the element from the front of the list.
- Time Complexity: O(n) (since all elements need to be shifted one position to the left)

**Peek Operation:**
- Return the first element of the list.
- Time Complexity: O(1)

**IsEmpty Operation:**
- Check if the list is empty.
- Time Complexity: O(1)

**Size Operation:**
- Return the length of the list.
- Time Complexity: O(1)

### Example Code Snippet for Simple Queue
```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def print_queue(self):
        print("Queue:", self.queue)
```

### Implementation of a Circular Queue Using a List

**Enqueue Operation:**
- Add the element at the rear position.
- Adjust the rear position using modulo operation to wrap around.
- Time Complexity: O(1)

**Dequeue Operation:**
- Remove the element from the front position.
- Adjust the front position using modulo operation to wrap around.
- Time Complexity: O(1)

**Peek Operation:**
- Return the element at the front position.
- Time Complexity: O(1)

**IsEmpty Operation:**
- Check if the queue is empty.
- Time Complexity: O(1)

**IsFull Operation:**
- Check if the queue is full.
- Time Complexity: O(1)

### Example Code Snippet for Circular Queue
```python
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is full")
            return
        elif (self.front == -1):
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if (self.front == -1):
            print("Queue is empty")
            return None
        data = self.queue[self.front]
        self.queue[self.front] = None
        if (self.front == self.rear):
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return data

    def peek(self):
        if (self.front == -1):
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def print_queue(self):
        print("Queue:", self.queue)
```

