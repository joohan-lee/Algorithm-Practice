# 34. Find First and Last Position of Element in Sorted Array

Acceptance: 40.3%
Difficulty: Medium
Frequency: 76.88%
Skills: Array, Binary Search
Solved: June 15, 2022

# Description

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

**You must write an algorithm with `O(log n)` runtime complexity.**

**Example 1:**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

```

**Example 2:**

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

```

**Example 3:**

```
Input: nums = [], target = 0
Output: [-1,-1]

```

**Constraints:**

- `0 <= nums.length <= 105`
- `109 <= nums[i] <= 109`
- `nums` is a non-decreasing array.
- `109 <= target <= 109`

# Solutions

### Python

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        
        left = 0
        right = n - 1
        min_idx = -1
        max_idx = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                min_idx = max_idx = mid
                
                mid_l = mid - 1
                while mid_l >=0 and nums[mid_l] == target:
                    mid_l -= 1
                min_idx = min(mid_l+1, min_idx)
                
                mid_r = mid + 1
                while mid_r < n and nums[mid_r] == target:
                    mid_r += 1
                max_idx = max(mid_r-1, max_idx)
                
                break
            
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
                
        return [min_idx, max_idx]
```

> Runtime: 144 ms, faster than 26.85% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.5 MB, less than 9.90% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
> 

### Complexity Analysis

- Time complexity : O(N), when all elements are target value, it takes O(N).
- Space complexity : O(1)

### Python

The code below is O(log N) solution.

It defines lower bound as an element which has same value as target and founded at left index or bigger than one elem before it.

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # Find the first target in nums
        lower_bound = self.findBound(nums, target, True)
        # if there is no target, return [-1,-1]
        if (lower_bound == -1):
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        return [lower_bound, upper_bound]
    
    def findBound(self, nums, target, isFirst):
        """
        :type nums: List[int]
        :type target: int
        :type isFist: bool
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = (left+right) // 2
            
            if nums[mid] == target:
                
                if isFirst:
                    # This means we found the first target element in nums, which means lower bound
                    if mid == left or nums[mid-1] < target:
                        return mid
                    # else, keep finding the first target on the left side
                    else:
                        right = mid - 1
                else:
                    if mid == right or nums[mid+1] > target:
                        return mid
                    else:
                        left = mid + 1
                
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1
```

> Runtime: 84 ms, faster than 96.43% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.4 MB, less than 49.30% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
> 

### Complexity Analysis

- Time complexity : O(log N), it performs binary search twice.
- Space complexity : O(1)

# Base Idea (One line)

1. Find lower bound and upper bound using Binary Search.

# Explanation

[Reference]

[Find First and Last Position of Element in Sorted Array - LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/)

Here is another similar solution from one user, [xxxleetcodexxx](https://leetcode.com/xxxleetcodexxx).

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        
        def searchLow(nums, target):
            head, tail = 0, len(nums) - 1
            while head <= tail:
                mid = (head + tail)//2
                if nums[mid] >= target:
                    tail = mid - 1
                else:
                    head = mid + 1
            return head
                
        def searchHigh(nums, target):
            head, tail = 0, len(nums) - 1
            while head <= tail:
                mid = (head + tail)//2
                if nums[mid] > target:
                    tail = mid - 1
                else:
                    head = mid + 1
            return tail
        
        start = searchLow(nums, target)
        end = searchHigh(nums, target)
        if 0 <= start < len(nums) and start <= end and nums[start] == target:
            return [start, end]
        else:
            return [-1, -1]
```