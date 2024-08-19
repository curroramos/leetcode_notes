from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

        Example 1:

        Input: grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
        ]
        Output: 1

        Example 2:

        Input: grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
        Output: 3

        Brute force:
        Loop on all the positions in the matrix. (not seen already) each time we visit a new position not in the set, we add a new island.

        Run DFS recursively to find all the values connected to the current position (up, down, left, right, checking not out of bounds). Save visited positions in a set.
        """
        
        def dfs(grid: List[List[str]], r: int, c: int, visit: set) -> None:
            # Check if the position is out of bounds or is water
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0' or (r, c) in visit:
                return
            # Mark the current cell as visited
            visit.add((r, c))
            # Recursively visit all adjacent cells
            dfs(grid, r - 1, c, visit)  # Up
            dfs(grid, r + 1, c, visit)  # Down
            dfs(grid, r, c - 1, visit)  # Left
            dfs(grid, r, c + 1, visit)  # Right
        
        num_islands = 0
        visit = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visit:
                    num_islands += 1
                    # Run DFS to mark the whole island
                    dfs(grid, r, c, visit)
        
        return num_islands
