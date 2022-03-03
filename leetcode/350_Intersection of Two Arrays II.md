# 350. Intersection of Two Arrays II

Acceptance: 0.546
Difficulty: Easy
Frequency: 0.4204
Skills: Array, Binary Search, Hash Table, Sorting, Two Pointers
Solved: February 28, 2022

# Description

Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

```

**Example 2:**

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

```

**Constraints:**

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

**Follow up:**

- What if the given array is already sorted? How would you optimize your algorithm?
- What if `nums1`'s size is small compared to `nums2`'s size? Which algorithm is better?
- What if elements of `nums2` are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# Solutions

### Python

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={}
        ret = []
        for i in range(len(nums1)):
            if nums1[i] in dict1:
                dict1[nums1[i]] += 1
            else:
                dict1[nums1[i]] = 1
        
        for i in range(len(nums2)):
            if nums2[i] in dict1 and dict1[nums2[i]] >= 1:
                ret.append(nums2[i])
                dict1[nums2[i]] -= 1
        
        return ret
```

> Runtime: 47 ms, faster than 90.40% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14.1 MB, less than 57.72% of Python3 online submissions for Intersection of Two Arrays II.
> 

### Complexity Analysis

- Time complexity : O(m+n), where m is the length of nums1, n is the length of nums2
- Space complexity : O(m), where m is the length of nums1

# Base Idea (One line)

1. Dictionary(Hash Map)을 이용하여 intersection search

# Explanation

[Reference]

[Intersection of Two Arrays II - LeetCode](https://leetcode.com/problems/intersection-of-two-arrays-ii/solution/)