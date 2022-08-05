# 347. Top K Frequent Elements

Acceptance: 64.9%
Difficulty: Medium
Frequency: 82.55%
Skills: Array, Bucket Sort, Counting, Divide and Conquer, Hash Table, Heap, Quickselect, Sorting
Solved: August 4, 2022

# Description

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]

```

**Constraints:**

- `1 <= nums.length <= 105`
- `104 <= nums[i] <= 104`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

# Solutions

### Python

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            if not num in h:
                h[num] = 1
            else:
                h[num] += 1
        h = sorted(h.items(), key =  lambda x: x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(h[i][0])
        return res
```

> Runtime: 132 ms, faster than 75.05% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.7 MB, less than 71.30% of Python3 online submissions for Top K Frequent Elements.
> 

### Complexity Analysis

- Time complexity : O(nlogn) for sorting
- Space complexity : O(n) for hash table

# Base Idea (One line)

1. Hash table and sorting
2. Hash table and Heap

# Explanation

[Reference]

[Top K Frequent Elements - LeetCode](https://leetcode.com/problems/top-k-frequent-elements/solution/)