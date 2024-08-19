### Sorting Algorithms Overview
Sorting is the process of arranging data in a specific order, typically in ascending or descending order. There are various sorting algorithms, each with its advantages and disadvantages. Understanding the different sorting algorithms is essential for solving problems efficiently.

### Common Sorting Algorithms

1. **Bubble Sort**
   - **Description:** Compares adjacent elements and swaps them if they are in the wrong order. Repeats this process until the list is sorted.
   - **Time Complexity:** O(n²)
   - **Space Complexity:** O(1) (in-place)
   - **Stability:** Stable

**Example Code:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

2. **Selection Sort**
   - **Description:** Divides the list into a sorted and unsorted region. Repeatedly selects the smallest element from the unsorted region and swaps it with the first unsorted element.
   - **Time Complexity:** O(n²)
   - **Space Complexity:** O(1) (in-place)
   - **Stability:** Not stable

**Example Code:**
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

3. **Insertion Sort**
   - **Description:** Builds the sorted array one element at a time by repeatedly picking the next element and inserting it into the correct position among the previously sorted elements.
   - **Time Complexity:** O(n²)
   - **Space Complexity:** O(1) (in-place)
   - **Stability:** Stable

**Example Code:**
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

4. **Merge Sort**
   - **Description:** A divide-and-conquer algorithm that splits the array into halves, recursively sorts each half, and then merges the sorted halves back together.
   - **Time Complexity:** O(n log n)
   - **Space Complexity:** O(n) (not in-place)
   - **Stability:** Stable

**Example Code:**
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
```

5. **Quick Sort**
   - **Description:** A divide-and-conquer algorithm that selects a pivot element, partitions the array around the pivot, and recursively sorts the partitions.
   - **Time Complexity:** O(n log n) on average, O(n²) in the worst case
   - **Space Complexity:** O(log n) (in-place)
   - **Stability:** Not stable

**Example Code:**
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
```

7. **Bucket Sort**
```python
def bucket_sort(arr):
    # Assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]
    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1
    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr
```

6. **Heap Sort**
   - **Description:** Builds a max heap from the array and then repeatedly extracts the maximum element from the heap, rebuilding the heap each time.
   - **Time Complexity:** O(n log n)
   - **Space Complexity:** O(1) (in-place)
   - **Stability:** Not stable

**Example Code:**
```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
```

7. **Counting Sort**
   - **Description:** Assumes that the input elements are integers within a known range. Counts the occurrences of each value and uses this information to place the elements in the correct position.
   - **Time Complexity:** O(n + k) where \( n \) is the number of elements and \( k \) is the range of the input
   - **Space Complexity:** O(k) (not in-place)
   - **Stability:** Stable

**Example Code:**
```python
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    index = 0
    for i, c in enumerate(count):
        while c > 0:
            arr[index] = i
            index += 1
            c -= 1
    return arr
```

8. **Radix Sort**
   - **Description:** Non-comparative sorting algorithm that sorts the elements by processing individual digits. It applies counting sort to each digit, starting from the least significant digit to the most significant digit.
   - **Time Complexity:** O(d(n + k)) where \( d \) is the number of digits and \( k \) is the range of the digit values
   - **Space Complexity:** O(n + k) (not in-place)
   - **Stability:** Stable

**Example Code:**
```python
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr
```

### Comparison of Sorting Algorithms
- **Bubble Sort, Selection Sort, Insertion Sort:**
  - Simple to implement and understand.
  - Inefficient for large datasets (O(n²) time complexity).

- **Merge Sort, Quick Sort, Heap Sort:**
  - More efficient for larger datasets (O(n log n) time complexity).
  - Merge Sort is stable and uses additional memory.
  - Quick Sort is efficient but not stable and has a worst-case time complexity of O(n²).
  - Heap Sort is not stable but is in-place.

- **Counting Sort, Radix Sort:**
  - Efficient for specific types of input (integer ranges).
  - Non-comparative algorithms with O(n + k) or O(d(n + k)) time complexity.
  - Require additional memory.

These notes cover the key concepts, implementations, and comparisons of various sorting algorithms. Let me know if you need more details or have any specific questions!