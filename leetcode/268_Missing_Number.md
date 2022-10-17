# 268. Missing Number

Acceptance: 61.5%
Difficulty: Easy
Frequency: 67.70%
Skills: Array, Binary Search, Hash Table, Math, Sorting, bit manipulation
Solved: October 16, 2022

# Description

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that is missing from the array.*

**Example 1:**

```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

```

**Example 2:**

```
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

```

**Example 3:**

```
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 104`
- `0 <= nums[i] <= n`
- All the numbers of `nums` are **unique**.

**Follow up:** Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?

# Solutions

### Python

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n+1) // 2
        sum_of_nums = 0
        for num in nums:
            sum_of_nums += num
            
        return total - sum_of_nums
```

> Runtime: 136 ms, faster than 96.36% of Python3 online submissions for Missing Number.
Memory Usage: 15.1 MB, less than 79.99% of Python3 online submissions for Missing Number.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(1)

# Base Idea (One line)

1. Find one missing value using Sorting, Hash set, or gauss’ formula.

# Explanation

[Reference]

[](https://leetcode.com/problems/missing-number/solution/)