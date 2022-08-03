# 215. Kth Largest Element in an Array

Acceptance: 65.1%
Difficulty: Medium
Frequency: 89.06%
Skills: Array, Divide and Conquer, Heap, Quickselect, Sorting
Solved: August 3, 2022

# Description

Given an integer array `nums` and an integer `k`, return *the* `kth` *largest element in the array*.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

You must solve it in `O(n)` time complexity.

**Example 1:**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

```

**Example 2:**

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

```

**Constraints:**

- `1 <= k <= nums.length <= 105`
- `104 <= nums[i] <= 104`

# Solutions

### Python

```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []
        
        for i in range(n):
            heapq.heappush(heap, nums[i])
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        # print(heap)
        return heap[0]
```

> Runtime: 983 ms, faster than 17.20% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 27.1 MB, less than 18.72% of Python3 online submissions for Kth Largest Element in an Array.
> 

### Complexity Analysis

- Time complexity : O(*N*log*k*).
- Space complexity : O(*k*) to store the heap elements

# Base Idea (One line)

1. heapq

# Explanation

[Reference]

[Kth Largest Element in an Array - LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/solution/)