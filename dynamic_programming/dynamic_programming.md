### Dynamic Programming Overview

Dynamic programming (DP) is an optimization technique used to solve complex problems by breaking them down into simpler subproblems. It is particularly useful for problems with overlapping subproblems and optimal substructure properties. DP stores the results of subproblems to avoid redundant computations, significantly improving efficiency.

### Key Concepts

1. **Overlapping Subproblems:** Problems that can be broken down into subproblems which are reused several times.
2. **Optimal Substructure:** The optimal solution to a problem can be constructed from the optimal solutions of its subproblems.
3. **Memoization:** Top-down approach that involves storing the results of expensive function calls and reusing them when the same inputs occur again.
4. **Tabulation:** Bottom-up approach that involves solving all possible subproblems and storing their results in a table (usually an array).

### Example Problems and Solutions

1. **Fibonacci Sequence**

   - **Problem:** Compute the n-th Fibonacci number.
   - **Recursive Solution:**
     ```python
     def fibonacci_recursive(n):
         if n <= 1:
             return n
         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

     # Example usage
     print(fibonacci_recursive(10))  # Output: 55
     ```

   - **Memoization Solution:**
     ```python
     def fibonacci_memoization(n, memo={}):
         if n in memo:
             return memo[n]
         if n <= 1:
             return n
         memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
         return memo[n]

     # Example usage
     print(fibonacci_memoization(10))  # Output: 55
     ```

   - **Tabulation Solution:**
     ```python
     def fibonacci_tabulation(n):
         if n <= 1:
             return n
         dp = [0] * (n + 1)
         dp[1] = 1
         for i in range(2, n + 1):
             dp[i] = dp[i - 1] + dp[i - 2]
         return dp[n]

     # Example usage
     print(fibonacci_tabulation(10))  # Output: 55
     ```

2. **Longest Common Subsequence (LCS)**

   - **Problem:** Given two sequences, find the length of their longest common subsequence.
   - **Recursive Solution:**
     ```python
     def lcs_recursive(X, Y, m, n):
         if m == 0 or n == 0:
             return 0
         if X[m - 1] == Y[n - 1]:
             return 1 + lcs_recursive(X, Y, m - 1, n - 1)
         else:
             return max(lcs_recursive(X, Y, m, n - 1), lcs_recursive(X, Y, m - 1, n))

     # Example usage
     X = "AGGTAB"
     Y = "GXTXAYB"
     print(lcs_recursive(X, Y, len(X), len(Y)))  # Output: 4
     ```

   - **Memoization Solution:**
     ```python
     def lcs_memoization(X, Y, m, n, memo={}):
         if (m, n) in memo:
             return memo[(m, n)]
         if m == 0 or n == 0:
             return 0
         if X[m - 1] == Y[n - 1]:
             memo[(m, n)] = 1 + lcs_memoization(X, Y, m - 1, n - 1, memo)
         else:
             memo[(m, n)] = max(lcs_memoization(X, Y, m, n - 1, memo), lcs_memoization(X, Y, m - 1, n, memo))
         return memo[(m, n)]

     # Example usage
     X = "AGGTAB"
     Y = "GXTXAYB"
     print(lcs_memoization(X, Y, len(X), len(Y)))  # Output: 4
     ```

   - **Tabulation Solution:**
     ```python
     def lcs_tabulation(X, Y):
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
     print(lcs_tabulation(X, Y))  # Output: 4
     ```

3. **0/1 Knapsack Problem**

   - **Problem:** Given weights and values of \( n \) items, put these items in a knapsack of capacity \( W \) to get the maximum total value in the knapsack.
   - **Recursive Solution:**
     ```python
     def knapsack_recursive(W, wt, val, n):
         if n == 0 or W == 0:
             return 0
         if wt[n - 1] > W:
             return knapsack_recursive(W, wt, val, n - 1)
         else:
             return max(val[n - 1] + knapsack_recursive(W - wt[n - 1], wt, val, n - 1),
                        knapsack_recursive(W, wt, val, n - 1))

     # Example usage
     val = [60, 100, 120]
     wt = [10, 20, 30]
     W = 50
     n = len(val)
     print(knapsack_recursive(W, wt, val, n))  # Output: 220
     ```

   - **Memoization Solution:**
     ```python
     def knapsack_memoization(W, wt, val, n, memo={}):
         if (W, n) in memo:
             return memo[(W, n)]
         if n == 0 or W == 0:
             return 0
         if wt[n - 1] > W:
             memo[(W, n)] = knapsack_memoization(W, wt, val, n - 1, memo)
         else:
             memo[(W, n)] = max(val[n - 1] + knapsack_memoization(W - wt[n - 1], wt, val, n - 1, memo),
                                knapsack_memoization(W, wt, val, n - 1, memo))
         return memo[(W, n)]

     # Example usage
     val = [60, 100, 120]
     wt = [10, 20, 30]
     W = 50
     n = len(val)
     print(knapsack_memoization(W, wt, val, n))  # Output: 220
     ```

   - **Tabulation Solution:**
     ```python
     def knapsack_tabulation(W, wt, val):
         n = len(val)
         dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
         for i in range(n + 1):
             for w in range(W + 1):
                 if i == 0 or w == 0:
                     dp[i][w] = 0
                 elif wt[i - 1] <= w:
                     dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
                 else:
                     dp[i][w] = dp[i - 1][w]
         return dp[n][W]

     # Example usage
     val = [60, 100, 120]
     wt = [10, 20, 30]
     W = 50
     print(knapsack_tabulation(W, wt, val))  # Output: 220
     ```

### Advantages and Disadvantages

**Advantages:**
- **Efficiency:** Avoids redundant calculations, making it much faster than naive recursive approaches.
- **Clarity:** Often leads to clear and simple code when compared to iterative solutions.

**Disadvantages:**
- **Memory Usage:** Requires additional memory to store the results of subproblems.
- **Complexity:** Can be difficult to identify subproblems and dependencies in some cases.

### Applications

1. **Optimization Problems:** Such as knapsack, scheduling, and resource allocation.
2. **String Processing:** Such as longest common subsequence, edit distance, and pattern matching.
3. **Combinatorial Problems:** Such as counting paths in graphs, partitioning sets, and bin packing.
4. **Games and Puzzles:** Such as tic-tac-toe, chess, and Sudoku.
