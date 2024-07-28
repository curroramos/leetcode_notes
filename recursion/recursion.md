### Recursion Overview
Recursion is a programming technique where a function calls itself in order to solve a problem. It typically involves breaking a problem down into smaller subproblems of the same type.

### Key Concepts
1. **Base Case:** The condition under which the recursion ends. It prevents the function from calling itself indefinitely.
2. **Recursive Case:** The part of the function that calls itself with modified arguments, gradually approaching the base case.

### Advantages of Recursion
- **Simplicity:** Makes code easier to write and understand, especially for problems that have a natural recursive structure (e.g., tree traversal, factorial calculation).
- **Reduction of Complex Problems:** Breaks down complex problems into simpler subproblems.

### Disadvantages of Recursion
- **Memory Usage:** Can consume a lot of memory due to the function call stack, especially for deep recursion.
- **Performance:** Recursive solutions can be slower and less efficient than iterative solutions due to overhead from multiple function calls.

### Common Recursive Problems
1. **Factorial Calculation:**
   - The factorial of a non-negative integer \( n \) is the product of all positive integers less than or equal to \( n \).
   - Formula: \( n! = n \times (n-1)! \) with \( 0! = 1 \) (base case).

**Example Code:**
```python
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case
```

2. **Fibonacci Sequence:**
   - The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
   - Formula: \( F(n) = F(n-1) + F(n-2) \) with \( F(0) = 0 \) and \( F(1) = 1 \) (base cases).

**Example Code:**
```python
def fibonacci(n):
    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
```

3. **Binary Search:**
   - Binary search is a search algorithm that finds the position of a target value within a sorted array.
   - It works by repeatedly dividing the search interval in half.
   - If the target value is less than the middle element, it searches the left half, otherwise it searches the right half.

**Example Code:**
```python
def binary_search(arr, target, low, high):
    if low > high:  # Base case
        return -1  # Target not found
    mid = (low + high) // 2
    if arr[mid] == target:  # Base case
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)  # Recursive case
    else:
        return binary_search(arr, target, mid + 1, high)  # Recursive case
```

4. **Tower of Hanoi:**
   - A mathematical puzzle where you have three rods and \( n \) disks. The objective is to move all the disks from the source rod to the destination rod using the auxiliary rod.
   - Rules:
     - Only one disk can be moved at a time.
     - A disk can only be placed on top of a larger disk.

**Example Code:**
```python
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:  # Base case
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)  # Move n-1 disks from source to auxiliary
    print(f"Move disk {n} from {source} to {destination}")  # Move the nth disk from source to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)  # Move n-1 disks from auxiliary to destination
```

### Tail Recursion
- Tail recursion is a special form of recursion where the recursive call is the last operation in the function.
- It allows some compilers and interpreters to optimize the recursion, reducing the risk of stack overflow and improving performance.

**Example of Tail Recursion:**
```python
def tail_recursive_factorial(n, accumulator=1):
    if n == 0:  # Base case
        return accumulator
    else:
        return tail_recursive_factorial(n - 1, n * accumulator)  # Recursive case with accumulator
```

### Recursion vs. Iteration
- Recursion involves function calls and can be less efficient in terms of memory and performance.
- Iteration uses loops and is generally more efficient.
- Some problems are naturally recursive and more intuitive to solve with recursion, while others are better suited for iterative solutions.

### Tips for Writing Recursive Functions
1. **Identify the Base Case:** Clearly define the condition under which the recursion stops.
2. **Ensure Progress Towards Base Case:** Make sure each recursive call brings the problem closer to the base case.
3. **Avoid Redundant Computations:** Use memoization or dynamic programming to store intermediate results and avoid redundant calculations.
4. **Consider Stack Overflow:** Be aware of the maximum recursion depth and consider iterative solutions or tail recursion for deep recursions.
