# 48. Rotate Image

Acceptance: 68.0%
Difficulty: Medium
Frequency: 82.08%
Skills: Array, Math, Matrix
Solved: July 30, 2022

# Description

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

```

**Constraints:**

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `1000 <= matrix[i][j] <= 1000`

# Solutions

### Python

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reverse(matrix)
        
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def reverse(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
```

> Runtime: 52 ms, faster than 59.82% of Python3 online submissions for Rotate Image.
Memory Usage: 14 MB, less than 29.73% of Python3 online submissions for Rotate Image.
> 

### Complexity Analysis

- Time complexity : O(M), O(M) for transposing and O(M) for reversing. We move the value of each cell once when transposing and reversing.
- Space complexity : O(1), because we do not use any other additional data structures.

# Base Idea (One line)

1. Transpose and Reverse

# Explanation

[Reference]

[Rotate Image - LeetCode](https://leetcode.com/problems/rotate-image/solution/)