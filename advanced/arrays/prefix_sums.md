### Prefix Sums Overview

Prefix sums are a powerful and efficient technique used to preprocess data to answer range sum queries quickly. The idea is to create an array of prefix sums where each element at index `i` contains the sum of all elements from the beginning of the array up to index `i`. This allows for quick calculations of the sum of any subarray.

### Key Concepts

1. **Prefix Sum Array:** An auxiliary array where each element at index `i` is the sum of the elements from the start of the original array to the index `i`.
2. **Range Sum Query:** Using the prefix sum array to quickly calculate the sum of any subarray in constant time.

### Example Problems and Solutions

1. **Calculate Prefix Sums**

   - **Problem:** Given an array, create a prefix sum array.
   - **Approach:** Iterate through the array, maintaining a running sum, and store it in the prefix sum array.

**Example Code:**
```python
def calculate_prefix_sums(arr):
    prefix_sums = [0] * len(arr)
    prefix_sums[0] = arr[0]

    for i in range(1, len(arr)):
        prefix_sums[i] = prefix_sums[i - 1] + arr[i]

    return prefix_sums

# Example usage
arr = [1, 2, 3, 4, 5]
print(calculate_prefix_sums(arr))  # Output: [1, 3, 6, 10, 15]
```

2. **Range Sum Query**

   - **Problem:** Given an array and multiple queries for the sum of elements between two indices, preprocess the array using prefix sums to answer the queries efficiently.
   - **Approach:** Use the prefix sum array to compute the sum of any subarray in constant time.

**Example Code:**
```python
def range_sum_query(arr, queries):
    prefix_sums = calculate_prefix_sums(arr)
    results = []

    for left, right in queries:
        if left == 0:
            results.append(prefix_sums[right])
        else:
            results.append(prefix_sums[right] - prefix_sums[left - 1])

    return results

# Example usage
arr = [1, 2, 3, 4, 5]
queries = [(0, 2), (1, 3), (0, 4)]
print(range_sum_query(arr, queries))  # Output: [6, 9, 15]
```

3. **Find Equilibrium Index**

   - **Problem:** Given an array, find the index where the sum of the elements on the left is equal to the sum of the elements on the right.
   - **Approach:** Use the prefix sum array to efficiently check for the equilibrium index.

**Example Code:**
```python
def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]

    return -1

# Example usage
arr = [1, 3, 5, 2, 2]
print(find_equilibrium_index(arr))  # Output: 2
```

4. **Count Number of Subarrays with Given Sum**

   - **Problem:** Given an array and a target sum, count the number of subarrays that sum up to the target sum.
   - **Approach:** Use a hashmap to store the prefix sums and their frequencies to count the subarrays efficiently.

**Example Code:**
```python
def count_subarrays_with_sum(arr, target):
    prefix_sum_count = {}
    prefix_sum = 0
    count = 0

    for num in arr:
        prefix_sum += num
        if prefix_sum == target:
            count += 1
        if (prefix_sum - target) in prefix_sum_count:
            count += prefix_sum_count[prefix_sum - target]
        if prefix_sum in prefix_sum_count:
            prefix_sum_count[prefix_sum] += 1
        else:
            prefix_sum_count[prefix_sum] = 1

    return count

# Example usage
arr = [1, 1, 1]
target = 2
print(count_subarrays_with_sum(arr, target))  # Output: 2
```

### Applications of Prefix Sums

1. **Range Queries:** Efficiently answering range sum queries and other range-based problems.
2. **Subarray Problems:** Counting subarrays with a given sum or finding the maximum sum subarray.
3. **Cumulative Frequency:** Useful in problems involving cumulative frequencies or cumulative distributions.
4. **Equilibrium Problems:** Finding equilibrium indices or balancing points in an array.

### Advantages and Disadvantages

**Advantages:**
- **Efficiency:** Reduces the time complexity of range sum queries to O(1) after an O(n) preprocessing step.
- **Simplicity:** Easy to implement and understand.

**Disadvantages:**
- **Space Complexity:** Requires additional space for the prefix sum array.
- **Limited Scope:** Specifically useful for sum-based queries and problems.

These notes cover the key concepts, example problems, and applications of prefix sums. Let me know if you need more details or have any specific questions!