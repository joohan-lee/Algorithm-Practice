# 31. Next Permutation

Acceptance: 36.9%
Difficulty: Medium
Frequency: 90.88%
Skills: Array, Two Pointers
Solved: September 2, 2022

# Description

A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

- For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: `[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

- For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`.
- Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`.
- While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, *find the next permutation of* `nums`.

The replacement must be **[in place](http://en.wikipedia.org/wiki/In-place_algorithm)** and use only constant extra memory.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [1,3,2]

```

**Example 2:**

```
Input: nums = [3,2,1]
Output: [1,2,3]

```

**Example 3:**

```
Input: nums = [1,1,5]
Output: [1,5,1]

```

**Constraints:**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

# Solutions

### Python

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # in-place로 해야하므로 pointer들로 찾는 수 밖에 없을 듯.
        # Find the first decreasing element from right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # Find the last element larger than nums[i]
        if i < 0:
            nums[:] = nums[::-1]
        else:
            j = i + 1
            while j < len(nums) and nums[j] > nums[i]:
                j += 1
            j -= 1

            # Swap them
            nums[i], nums[j] = nums[j], nums[i]

            # Reverse elements behind the first pointer
            nums[i+1:len(nums)] = nums[len(nums)-1:i:-1]
```

> Runtime: 97 ms, faster than 5.03% of Python3 online submissions for Next Permutation.
Memory Usage: 13.8 MB, less than 74.31% of Python3 online submissions for Next Permutation.
> 

### Complexity Analysis

- Time complexity : O(N), In worst case, only two scans of the whole array are needed.
- Space complexity : O(1). In place replacements are done.

# Base Idea (One line)

1. Focus on we need right “next” larger one.

# Explanation

[Reference]

[Next Permutation - LeetCode](https://leetcode.com/problems/next-permutation/solution/)