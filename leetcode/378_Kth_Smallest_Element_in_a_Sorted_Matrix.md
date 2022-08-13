# 378. Kth Smallest Element in a Sorted Matrix

Acceptance: 61.4%
Difficulty: Medium
Frequency: 63.54%
Skills: Array, Binary Search, Heap, Matrix, Sorting
Solved: August 12, 2022

# Description

Given an `n x n` `matrix` where each of the rows and columns is sorted in ascending order, return *the* `kth` *smallest element in the matrix*.

Note that it is the `kth` smallest element **in the sorted order**, not the `kth` **distinct** element.

You must find a solution with a memory complexity better than `O(n2)`.

**Example 1:**

```
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

```

**Example 2:**

```
Input: matrix = [[-5]], k = 1
Output: -5

```

**Constraints:**

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 300`
- `109 <= matrix[i][j] <= 109`
- All the rows and columns of `matrix` are **guaranteed** to be sorted in **non-decreasing order**.
- `1 <= k <= n2`

**Follow up:**

- Could you solve the problem with a constant memory (i.e., `O(1)` memory complexity)?
- Could you solve the problem in `O(n)` time complexity? The solution may be too advanced for an interview but you may find reading [this paper](http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf) fun.

# Solutions

### Python

```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # create min heap
        heap = []
        
        n = len(matrix)
        # get min(n,k) elements from first column of matrix
        for r in range(min(n,k)):
            heap.append((matrix[r][0],r,0))
        
        heapq.heapify(heap)
        
        # until we find k elements
        while k > 0:
            # extract min element
            curr_tuple = heapq.heappop(heap)
            curr_val = curr_tuple[0]
            curr_row = curr_tuple[1]
            curr_col = curr_tuple[2]
            # If we have any new elements in the current row, add them
            if curr_col < n - 1:
                heapq.heappush(heap, (matrix[curr_row][curr_col+1], curr_row, curr_col+1))
            
            # decrement k
            k -= 1
            
        
        return curr_val
```

> Runtime: 356 ms, faster than 31.79% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.8 MB, less than 38.85% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
> 

### Complexity Analysis

- Time complexity : let X = min(N,K); O(X + Klog(X))
    - Well the heap construction takes O(X) time
    - K iterations with extracting and adding operations on Min-heap. Each operation takes O(logX) time.
- Space complexity : O(X) which is occupied by heap

# Base Idea (One line)

1. Store triplet, **(value, row, col)**, into **heap** and use them as min(N,k) pointers.

# Explanation

[Reference]

[Kth Smallest Element in a Sorted Matrix - LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/)

There is another solution using Binary-search. Refer to the above link.