# 240. Search a 2D Matrix II

Acceptance: 50.5%
Difficulty: Medium
Frequency: 72.15%
Skills: Array, Binary Search, Divide and Conquer, Matrix
Solved: October 20, 2022
다시풀기: Once

# Description

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg](https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg)

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg](https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg)

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= n, m <= 300`
- `109 <= matrix[i][j] <= 109`
- All the integers in each row are **sorted** in ascending order.
- All the integers in each column are **sorted** in ascending order.
- `109 <= target <= 109`

# Solutions

### Python

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, target):
            left= 0
            right = len(arr) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                if target == arr[mid]:
                    return True
                elif target > arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return False
        
        for row in matrix:
            if binary_search(row, target):
                return True
        
        return False
```

> Runtime: 
Memory Usage:
> 

### Complexity Analysis

- Time complexity : O(mlogn)
- Space complexity : O(1)

### D & C

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def searchRec(left, right, up, down):
            # Rectangle
            #(up,left)      (up,right)
            #(down,left)    (down,right)
            
            # this submatrix(rectangle) has no height or no width.
            if left> right or up > down:
                return False
            # if target is outside of submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
            
            mid = left + (right-left) // 2
            
            # locate 'row' such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
                
            return searchRec(left, mid-1, row, down) or searchRec(mid+1, right, up, row-1)
        
        return searchRec(0, len(matrix[0])-1, 0, len(matrix)-1)
```

Runtime: 176 ms, faster than 94.08% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 21.1 MB, less than 5.61% of Python3 online submissions for Search a 2D Matrix II.

O(nlogn) time

O(logn) space. Since the recursion tree has ‘logn’ height.

### 3. ****Search Space Reduction****

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # cache m, n as they won't change
        height = len(matrix)
        width = len(matrix[0])
        
        # start our pointer from the bottom-left
        row = height - 1
        col = 0
        
        while row >=0 and col < width:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
            
        return False
```

Runtime: 289 ms, faster than 69.82% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 20.4 MB, less than 83.62% of Python3 online submissions for Search a 2D Matrix II.

O(m+n) time.

O(1) space.

# Base Idea (One line)

1. Since it is already sorted, we can use binary search. We can use also D&C.
2. Since row and col are sorted, if we start from bottom-left, we can reduce search space in one way.

# Explanation

[Reference]

[Search a 2D Matrix II - LeetCode](https://leetcode.com/problems/search-a-2d-matrix-ii/solution/)