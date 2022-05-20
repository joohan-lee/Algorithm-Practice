# 136. Single Number

Acceptance: 69.4%
Difficulty: Easy
Frequency: 66.25%
Skills: Array, bit manipulation
Solved: May 19, 2022

# Description

Given a **non-empty** array of integers `nums`, every element appears *twice* except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

**Example 1:**

```
Input: nums = [2,2,1]
Output: 1

```

**Example 2:**

```
Input: nums = [4,1,2,1,2]
Output: 4

```

**Example 3:**

```
Input: nums = [1]
Output: 1

```

**Constraints:**

- `1 <= nums.length <= 3 * 104`
- `3 * 104 <= nums[i] <= 3 * 104`
- Each element in the array appears twice except for one element which appears only once.

# Solutions

### Python

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for num in nums:
            # XOR
            n = n^num
        return n
```

> Runtime: 221 ms, faster than 34.45% of Python3 online submissions for Single Number.
Memory Usage: 16.8 MB, less than 21.06% of Python3 online submissions for Single Number.
> 

### Complexity Analysis

- Time complexity : O(n), where n is the length of nums
- Space complexity : O(1)

# Base Idea (One line)

1. Bit Manipulation (XOR - 0 only if both are same)

# Explanation

[Reference]

[Single Number - LeetCode](https://leetcode.com/problems/single-number/solution/)