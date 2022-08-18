# 64. Minimum Path Sum

Acceptance: 60.2%
Difficulty: Medium
Frequency: 61.23%
Skills: Array, Dynamic Programming, Matrix
Solved: August 17, 2022

# Description

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)

```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

```

**Example 2:**

```
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 100`

# Solutions

### Python

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0] * col for _ in range(row)]
        
        dp[0][0] = grid[0][0]
        for i in range(1, col):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for i in range(1, row):
            for j in range(1,col):
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        
        return dp[row-1][col-1]
```

> Runtime: 211 ms, faster than 16.86% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15.7 MB, less than 54.33% of Python3 online submissions for Minimum Path Sum.
> 

### Complexity Analysis

- Time complexity : O(MN)
- Space complexity : O(MN)

# Base Idea (One line)

1. 2D Dynamic Programming. 

# Explanation

[Reference]

[Minimum Path Sum - LeetCode](https://leetcode.com/problems/minimum-path-sum/solution/)