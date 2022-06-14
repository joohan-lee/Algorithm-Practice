# 33. Search in Rotated Sorted Array

Acceptance: 38.0%
Difficulty: Medium
Frequency: 82.23%
Skills: Array, Binary Search
Solved: June 13, 2022

# Description

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`*, or* `-1` *if it is not in* `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

```

**Example 3:**

```
Input: nums = [1], target = 0
Output: -1

```

**Constraints:**

- `1 <= nums.length <= 5000`
- `104 <= nums[i] <= 104`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- `104 <= target <= 104`

# Solutions

### Python

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_rotate_index(left,right):
            if nums[left] < nums[right]:
                return 0
            
            while left <= right:
                pivot = (left + right) // 2
                
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                
                if nums[pivot] < nums[left]:
                    right = pivot - 1
                else:
                    left = pivot + 1
        
        def search(left, right):
            """
            Binary Search
            """
            
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
            
            
        
        n = len(nums)
        
        if n==1:
            return 0 if nums[0] == target else -1
        rotate_index = find_rotate_index(0,n-1)
        
        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n-1)
        
        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n-1)
        # search on the left side
        else:
            return search(0, rotate_index - 1)
```

> Runtime: 56 ms, faster than 54.73% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.5 MB, less than 18.15% of Python3 online submissions for Search in Rotated Sorted Array.
> 

### Complexity Analysis

- Time complexity : O(logN)
- Space complexity : O(1)

# Base Idea (One line)

1. 오름차순 정렬되어있었으므로 pivot은 가장 작은 element이고, 이는 이웃한 값을 비교하여 찾을 수 있다.

# Explanation

[Reference]

[Search in Rotated Sorted Array - LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/)

one-pass binary search solution도 있으니 참고.