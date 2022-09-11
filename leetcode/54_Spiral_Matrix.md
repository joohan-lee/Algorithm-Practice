# 54. Spiral Matrix

Acceptance: 43.1%
Difficulty: Medium
Frequency: 87.30%
Skills: Array, Matrix
Solved: September 9, 2022

# Description

Given an `m x n` `matrix`, return *all elements of the* `matrix` *in spiral order*.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `100 <= matrix[i][j] <= 100`

# Solutions

### Python

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h = len(matrix)
        w = len(matrix[0])
        up = 0
        left = 0
        down = h - 1
        right = w - 1
        
        ans = []
        while len(ans) < w * h:
            # move right
            for col in range(left, right + 1):
                ans.append(matrix[up][col])
            
            # move down
            for row in range(up + 1, down + 1):
                ans.append(matrix[row][right])
            
            # move left if up != down
            # up이랑 down이 같다는건 이미 위 move right에서 방문했다는 뜻
            if up != down:
                for col in range(right-1, left - 1, -1):
                    ans.append(matrix[down][col])
            
            # move up if left != right
            # left랑 right이 같다는건 이미 위 move down에서 방문했다는 뜻
            if left != right:
                for row in range(down - 1, up, -1):
                    ans.append(matrix[row][left])
            
            up += 1
            left += 1
            down -=1
            right -= 1
            
        return ans
```

> Runtime: 55 ms, faster than 31.67% of Python3 online submissions for Spiral Matrix.
Memory Usage: 14 MB, less than 33.76% of Python3 online submissions for Spiral Matrix.
> 

### Complexity Analysis

- Time complexity : O(MN)
- Space complexity : O(1)

# Base Idea (One line)

1. repeat moving 4 directions

# Explanation

[Reference]

[Spiral Matrix - LeetCode](https://leetcode.com/problems/spiral-matrix/solution/)