### Binary Search Overview
Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeat until the value is found or the interval is empty.

### Key Concepts
1. **Precondition:** The list must be sorted.
2. **Divide and Conquer:** The algorithm divides the search space in half during each step.
3. **Logarithmic Time Complexity:** The time complexity of binary search is O(log n), making it very efficient for large datasets.

### Steps of Binary Search
1. **Initialization:** Set two pointers, `low` to the first element and `high` to the last element of the list.
2. **Iteration:**
   - Calculate the middle index: `mid = (low + high) // 2`.
   - Compare the middle element with the target value:
     - If they are equal, return the middle index.
     - If the target is smaller than the middle element, narrow the search to the lower half: `high = mid - 1`.
     - If the target is larger than the middle element, narrow the search to the upper half: `low = mid + 1`.
3. **Termination:** The search ends when the `low` pointer exceeds the `high` pointer. If the target value is not found, return -1.

### Example Code: Iterative Binary Search
```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
print(binary_search(arr, target))  # Output: 6
```

### Example Code: Recursive Binary Search
```python
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
print(binary_search_recursive(arr, target, 0, len(arr) - 1))  # Output: 6
```

### Variations of Binary Search
1. **Finding the First or Last Occurrence:**
   - To find the first occurrence of a target value, modify the algorithm to continue searching in the left half even if the target is found.
   - To find the last occurrence, continue searching in the right half.

**Example Code for Finding the First Occurrence:**
```python
def binary_search_first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

# Example usage
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(binary_search_first_occurrence(arr, target))  # Output: 1
```

2. **Finding the Insertion Point:**
   - Useful for finding where a new element should be inserted in a sorted array to maintain the order.

**Example Code for Finding the Insertion Point:**
```python
def binary_search_insertion_point(arr, target):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low

# Example usage
arr = [1, 2, 4, 5]
target = 3
print(binary_search_insertion_point(arr, target))  # Output: 2
```

### Advantages of Binary Search
- **Efficiency:** O(log n) time complexity makes it suitable for large datasets.
- **Simplicity:** Easy to implement and understand.

### Disadvantages of Binary Search
- **Requires Sorted Data:** The array must be sorted before performing binary search.
- **Complexity for Small Data:** Linear search might be more efficient for very small datasets.

### Applications of Binary Search
- **Searching in Sorted Arrays:** Quickly find elements in a sorted list.
- **Dictionary Lookups:** Efficiently search for words or keys in a sorted dictionary.
- **Finding Boundaries:** Determine the range of values within a certain threshold in a sorted dataset.
- **Algorithm Optimization:** Used in various algorithms to optimize search operations, such as in binary search trees.
