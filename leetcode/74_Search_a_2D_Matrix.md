# 74. Search a 2D Matrix

Acceptance: 46.4%
Difficulty: Medium
Frequency: 72.17%
Skills: Array, Binary Search, Matrix
Solved: September 13, 2022

# Description

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/10/05/mat.jpg](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `104 <= matrix[i][j], target <= 104`

# Solutions

### Python

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row, lo, hi):
            
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if target == matrix[row][mid]:
                    return True
                elif target> matrix[row][mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        ans = False
        for r in range(m):
            if target >= matrix[r][0] and target <= matrix[r][n-1]:
                ans = binary_search(r, 0, n-1)
        
        return ans
```

> Runtime: 72 ms, faster than 49.38% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.4 MB, less than 43.23% of Python3 online submissions for Search a 2D Matrix.
> 

### Complexity Analysis

- Time complexity : O(mlogn)
- Space complexity : O(1)

# Base Idea (One line)

1. When matrix consider as a vector, the row in matrix is idx // n and col is idx % n.

# Explanation

[Reference]

[Search a 2D Matrix - LeetCode](https://leetcode.com/problems/search-a-2d-matrix/solution/)

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        lo = 0
        hi = m*n -1
        
        while lo <= hi:
            pivot_idx = lo + (hi-lo) // 2
            pivot_elem = matrix[pivot_idx//n][pivot_idx%n]
            if target == pivot_elem:
                return True
            elif target > pivot_elem:
                lo = pivot_idx + 1
            else:
                hi = pivot_idx - 1
        return False
```

Runtime: 73 ms, faster than 47.53% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.3 MB, less than 88.96% of Python3 online submissions for Search a 2D Matrix.

Time: O(log(mn))

Space: O(1)