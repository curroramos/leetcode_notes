### 2D Dynamic Programming Overview

2D dynamic programming extends the concept of dynamic programming to two dimensions. This approach is used when the problem involves a grid or matrix and requires solving subproblems that depend on two indices.

### Key Concepts

1. **DP Table:** A 2D array (or matrix) where each cell represents the solution to a subproblem.
2. **State Transition:** The value of each cell is computed based on the values of its neighboring cells.
3. **Initialization:** Setting up the base cases, often the first row and first column of the DP table.
4. **Filling the DP Table:** Using nested loops to fill the table based on the state transition.

### Example Problems and Solutions

1. **Longest Common Subsequence (LCS)**

   - **Problem:** Given two sequences, find the length of their longest common subsequence.
   - **DP Table Definition:** `dp[i][j]` represents the length of the LCS of the first `i` characters of sequence `X` and the first `j` characters of sequence `Y`.

**Example Code:**
```python
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
print(lcs(X, Y))  # Output: 4
```

2. **0/1 Knapsack Problem**

   - **Problem:** Given weights and values of `n` items, put these items in a knapsack of capacity `W` to get the maximum total value in the knapsack.
   - **DP Table Definition:** `dp[i][w]` represents the maximum value that can be obtained with the first `i` items and a knapsack capacity of `w`.

**Example Code:**
```python
def knapsack(W, wt, val):
    n = len(val)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Example usage
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print(knapsack(W, wt, val))  # Output: 220
```

3. **Minimum Path Sum in a Grid**

   - **Problem:** Given a `m x n` grid filled with non-negative numbers, find a path from the top-left to the bottom-right which minimizes the sum of all numbers along its path.
   - **DP Table Definition:** `dp[i][j]` represents the minimum path sum to reach cell `(i, j)` from the top-left corner.

**Example Code:**
```python
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[m - 1][n - 1]

# Example usage
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(min_path_sum(grid))  # Output: 7
```

4. **Edit Distance**

   - **Problem:** Given two strings `word1` and `word2`, find the minimum number of operations required to convert `word1` to `word2`. Operations allowed are insert a character, remove a character, or replace a character.
   - **DP Table Definition:** `dp[i][j]` represents the minimum number of operations required to convert the first `i` characters of `word1` to the first `j` characters of `word2`.

**Example Code:**
```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[m][n]

# Example usage
word1 = "kitten"
word2 = "sitting"
print(edit_distance(word1, word2))  # Output: 3
```

### Advantages and Disadvantages

**Advantages:**
- **Efficiency:** Avoids redundant calculations, making it much faster than naive recursive approaches.
- **Clarity:** Often leads to clear and simple code when compared to iterative solutions.

**Disadvantages:**
- **Memory Usage:** Requires additional memory to store the results of subproblems.
- **Complexity:** Can be difficult to identify subproblems and dependencies in some cases.

### Applications

1. **Grid-Based Problems:** Such as minimum path sum, maximum path sum, and obstacle avoidance.
2. **String Processing:** Such as longest common subsequence, edit distance, and pattern matching.
3. **Combinatorial Problems:** Such as counting paths in graphs, partitioning sets, and bin packing.
4. **Optimization Problems:** Such as knapsack, scheduling, and resource allocation.
