# 1. Two Sum

Acceptance: 0.483
Difficulty: Easy
Frequency: 1
Skills: Hash Table, array
Solved: February 21, 2022

# Description

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

```

**Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]

```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]

```

**Constraints:**

- `2 <= nums.length <= 104`
- `109 <= nums[i] <= 109`
- `109 <= target <= 109`
- **Only one valid answer exists.**

# Solutions

### Python

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    ret.extend([i,j])
                    return ret
```

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        n = len(nums)
        for i in range(n):
            dict[nums[i]] = i
        for i in range(n):
            complement = target - nums[i]
            if complement in dict and dict[complement] != i:
                return [i,dict[complement]]
```

> Runtime: **64 ms**
Memory Usage: **15.2 MB**
> 

### Complexity Analysis

- Time complexity :  O(n^2) - Brute Force, O(n) - Hash Table(because lookup in dictionary takes O(1)).
- Space complexity : O(n)

# Base Idea (One line)

Hash Table을 이용하여 O(1)으로 complement를 찾을 수 있는가 

# Explanation

[Reference]

[Two Sum - LeetCode](https://leetcode.com/problems/two-sum/solution/)