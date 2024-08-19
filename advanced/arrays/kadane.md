### Kadane's Algorithm Overview

Kadane's Algorithm is a popular and efficient technique used to solve the "Maximum Subarray Sum" problem. This algorithm is designed to find the contiguous subarray within a one-dimensional array of numbers which has the largest sum.

### Key Concepts

1. **Dynamic Programming:** Kadane's Algorithm uses a dynamic programming approach to solve the problem in linear time.
2. **Subarray Sum:** It maintains a running sum of the current subarray and updates the maximum sum found so far.

### Problem Statement

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

### Algorithm Steps

1. Initialize two variables:
   - `max_current` to track the current subarray sum.
   - `max_global` to track the maximum subarray sum found so far.
2. Iterate through the array:
   - Update `max_current` to be the maximum of the current element itself or the current element plus `max_current`.
   - Update `max_global` if `max_current` is greater than `max_global`.
3. Return `max_global` as the result.

### Example Code

```python
def kadane_algorithm(nums):
    if not nums:
        return 0
    
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
    
    return max_global

# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane_algorithm(nums))  # Output: 6 (subarray: [4, -1, 2, 1])
```

### Explanation

1. **Initialization:**
   - `max_current` and `max_global` are both set to the first element of the array.

2. **Iteration:**
   - For each element in the array (starting from the second element), update `max_current` to be the maximum of the current element or the current element plus `max_current`. This step decides whether to start a new subarray at the current element or to extend the existing subarray.
   - Update `max_global` if `max_current` is greater than `max_global`. This step keeps track of the maximum subarray sum found so far.

3. **Return Result:**
   - The final value of `max_global` is the maximum subarray sum.

### Handling Edge Cases

1. **Empty Array:**
   - If the input array is empty, the function returns 0.
   
2. **All Negative Numbers:**
   - Kadane's Algorithm works correctly even if all numbers are negative. The maximum subarray sum will be the largest single element (since adding two negative numbers results in a smaller number).

### Variations

1. **Finding the Subarray Itself:**
   - Modify the algorithm to keep track of the start and end indices of the maximum subarray.

**Example Code:**
```python
def kadane_with_indices(nums):
    if not nums:
        return 0, -1, -1
    
    max_current = max_global = nums[0]
    start = end = s = 0
    
    for i in range(1, len(nums)):
        if nums[i] > max_current + nums[i]:
            max_current = nums[i]
            s = i
        else:
            max_current += nums[i]
        
        if max_current > max_global:
            max_global = max_current
            start = s
            end = i
    
    return max_global, start, end

# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, start, end = kadane_with_indices(nums)
print(max_sum)  # Output: 6
print(nums[start:end + 1])  # Output: [4, -1, 2, 1]
```

### Applications

1. **Financial Analysis:** Finding the maximum profit that can be made by buying and selling stocks over a period.
2. **Signal Processing:** Finding the maximum sum segment in signal data.
3. **Game Development:** Optimizing scores or values in gaming scenarios.
4. **Data Analysis:** Analyzing and identifying significant patterns in datasets.

### Advantages and Disadvantages

**Advantages:**
- **Efficiency:** Linear time complexity O(n), making it suitable for large datasets.
- **Simplicity:** Easy to implement and understand.

**Disadvantages:**
- **Limited Scope:** Specifically designed for one-dimensional arrays. For multi-dimensional arrays, modifications are needed.
- **Not Generalized:** The algorithm works only for problems related to maximum subarray sum.

These notes cover the key concepts, implementation, variations, and applications of Kadane's Algorithm. Let me know if you need more details or have any specific questions!