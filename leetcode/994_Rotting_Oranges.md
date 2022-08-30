# 994. Rotting Oranges

Acceptance: 52.2%
Difficulty: Medium
Frequency: 72.96%
Skills: Array, BFS, Matrix
Solved: August 29, 2022

# Description

You are given an `m x n` `grid` where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1`.

**Example 1:**

![https://assets.leetcode.com/uploads/2019/02/16/oranges.png](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

```

**Example 2:**

```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

```

**Example 3:**

```
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

# Solutions

### Python

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # bfs
        # For initial state, find all rotten oranges and add them into queue,
        # and find the total number of fresh oranges -> BFS 끝냈는데 여전히 fresh one 남아있는지 확인 위함
        # queue를 두개 사용하여 한번 다 비울때 minute + 1
        # bfs 전부 끝냈는데 fresh orange 남아있다면 모두 썩는건 불가능함을 의미.
        freshOrange = 0
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    freshOrange += 1
                    
        
        
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        curr_n = len(q)
        minute = 0
        while q:
            r, c = q.popleft()
            curr_n -= 1
            for direction in directions:
                nr = r + direction[0]
                nc = c + direction[1]
                if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2 # 방문처리!!
                    q.append((nr,nc))
                    freshOrange-=1
            if curr_n == 0 and len(q) > 0:
                curr_n = len(q)
                minute += 1
        
        return minute if freshOrange == 0 else -1
```

> Runtime: 44 ms, faster than 99.44% of Python3 online submissions for Rotting Oranges.
Memory Usage: 13.9 MB, less than 91.77% of Python3 online submissions for Rotting Oranges.
> 

### Complexity Analysis

- Time complexity : O(mn). First, we scan the grid to find the initial values for the queue, O(mn).
    
    In the worst case, enumerate all cells in the grid using BFS, O(mn).
    
    O(mn) + O(mn) = O(mn)
    
- Space complexity : O(mn), in the worst case, the grid is filled with rotten oranges.

# Base Idea (One line)

1. Find initial rotten oranges and BFS from them.

# Explanation

[Reference]

[Rotting Oranges - LeetCode](https://leetcode.com/problems/rotting-oranges/solution/)