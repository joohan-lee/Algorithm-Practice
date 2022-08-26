# 200. Number of Islands

Acceptance: 55.2%
Difficulty: Medium
Frequency: 97.71%
Skills: Array, BFS, DFS, Matrix, Union Find
Solved: August 25, 2022

# Description

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

```

**Example 2:**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

# Solutions

### Python

### 1. DFS

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            for direction in directions:
                dfs(i + direction[0], j + direction[1])
            
        m = len(grid)
        n = len(grid[0])
        
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island += 1
                    dfs(i,j)
        
        return island
```

> Runtime: 272 ms, faster than 99.27% of Python3 online submissions for Number of Islands.
Memory Usage: 16.4 MB, less than 65.51% of Python3 online submissions for Number of Islands.
> 

### Complexity Analysis

- Time complexity : O(MN)
- Space complexity : O(MN)

### 2. BFS

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        m = len(grid)
        n = len(grid[0])
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island += 1
                    q = deque()
                    q.append((i,j))

                    while q:
                        elem = q.popleft()
                        r = elem[0]
                        c = elem[1]
                        if r < 0 or r >= m or c < 0 or c >= n:
                            continue
                        if grid[r][c] == '0':
                            continue
                        
                        grid[r][c] = '0'
                        for direction in directions:
                            q.append((r + direction[0], c + direction[1]))
        
        return island
```

> Runtime: 614 ms, faster than 22.72% of Python3 online submissions for Number of Islands.
Memory Usage: 16.3 MB, less than 81.67% of Python3 online submissions for Number of Islands.
> 

### Complexity Analysis

- Time complexity : O(MN)
- Space complexity : *O*(*min*(*M*,*N*)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(*M*,*N*).

# Base Idea (One line)

1. 2-dimensional DFS, BFS with 4 directions

# Explanation

[Reference]

[Number of Islands - LeetCode](https://leetcode.com/problems/number-of-islands/solution/)