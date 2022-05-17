# 35. Search Insert Position

Acceptance: 42.3%
Difficulty: Easy
Frequency: 58.95%
Skills: Array, Binary Search
Solved: May 17, 2022

# Description

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [1,3,5,6], target = 5
Output: 2

```

**Example 2:**

```
Input: nums = [1,3,5,6], target = 2
Output: 1

```

**Example 3:**

```
Input: nums = [1,3,5,6], target = 7
Output: 4

```

**Constraints:**

- `1 <= nums.length <= 104`
- `104 <= nums[i] <= 104`
- `nums` contains **distinct** values sorted in **ascending** order.
- `104 <= target <= 104`

# Solutions

### Python

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        start = 0
        end = n - 1
        
        while start <= end:
            mid = (start + end) // 2
            mid_val = nums[mid]
            
            if mid_val == target:
                return mid
            elif mid_val > target:
                end = mid - 1
            else:
                start = mid + 1

        if target < nums[0]:
            return 0
        elif target > nums[n-1]:
            return n
        elif target > nums[mid]:
            return (mid + 1)
        else:
            return mid
```

> Runtime: 58 ms, faster than 68.12% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.7 MB, less than 83.15% of Python3 online submissions for Search Insert Position.
> 

### Complexity Analysis

- Time complexity : O(log n), where n is the length of nums
- Space complexity : O(1)

# Base Idea (One line)

1. Binary search and be careful with return index(=start)

# Explanation

[Reference]

마지막에 start를 반환하면 if 조건문으로 edge case를 신경쓰지 않아도 된다.

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        start = 0
        end = n - 1
        
        while start <= end:
            mid = (start + end) // 2
            mid_val = nums[mid]
            
            if mid_val == target:
                return mid
            elif mid_val > target:
                end = mid - 1
            else:
                start = mid + 1

        return start
```

[Search Insert Position - LeetCode](https://leetcode.com/problems/search-insert-position/solution/)