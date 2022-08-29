# 75. Sort Colors

Acceptance: 56.5%
Difficulty: Medium
Frequency: 69.14%
Skills: Array, Sorting, Two Pointers
Solved: August 27, 2022

# Description

Given an array `nums` with `n` objects colored red, white, or blue, sort them **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

**Example 1:**

```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

```

**Example 2:**

```
Input: nums = [2,0,1]
Output: [0,1,2]

```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

**Follow up:** Could you come up with a one-pass algorithm using only constant extra space?

# Solutions

### Python

### 1. Selectin Sort

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
```

> Runtime: 51 ms, faster than 55.15% of Python3 online submissions for Sort Colors.
Memory Usage: 14 MB, less than 15.87% of Python3 online submissions for Sort Colors.
> 

### Complexity Analysis

- Time complexity : O(n^2)
- Space complexity : O(1)

### 2. Two Pointers

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        curr = 0
        
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
```

> Runtime: 34 ms, faster than 94.29% of Python3 online submissions for Sort Colors.
Memory Usage: 13.9 MB, less than 15.87% of Python3 online submissions for Sort Colors.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(1)

# Base Idea (One line)

1. Selection Sort or Use three pointers that store rightmost 0 index, leftmost 2 index, and curr point

# Explanation

[Reference]

[Sort Colors - LeetCode](https://leetcode.com/problems/sort-colors/solution/)