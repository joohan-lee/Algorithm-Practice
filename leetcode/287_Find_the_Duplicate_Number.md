# 287. Find the Duplicate Number

Acceptance: 59.0%
Difficulty: Medium
Frequency: 75.31%
Skills: Array, Binary Search, Two Pointers, bit manipulation
Solved: August 4, 2022

# Description

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return *this repeated number*.

You must solve the problem **without** modifying the array `nums` and uses only constant extra space.

**Example 1:**

```
Input: nums = [1,3,4,2,2]
Output: 2

```

**Example 2:**

```
Input: nums = [3,1,3,4,2]
Output: 3

```

**Constraints:**

- `1 <= n <= 105`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

**Follow up:**

- How can we prove that at least one duplicate number must exist in `nums`?
- Can you solve the problem in linear runtime complexity?

# Solutions

### Python

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
```

> Runtime: 1496 ms, faster than 6.53% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 27.8 MB, less than 91.14% of Python3 online submissions for Find the Duplicate Number.
> 

### Complexity Analysis

- Time Complexity: *O*(*n*log*n*)
    
    Sorting takes *O*(*n*log*n*) time. This is followed by a linear scan, resulting in a total of *O*(*n*log*n*) + *O*(*n*) = *O*(*n*log*n*) time.
    
- Space Complexity: *O*(log*n*) or *O*(*n*)
    
    The space complexity of the sorting algorithm depends on the implementation of each programming language:
    
    - In Java, Arrays.sort() for primitives is implemented using a variant of the Quick Sort algorithm, which has a space complexity of *O*(log*n*)
        
        O(\log n)
        
    - In C++, the sort() function provided by STL uses a hybrid of Quick Sort, Heap Sort and Insertion Sort, with a worst case space complexity of *O*(log*n*)
        
        O(\log n)
        
    - In Python, the sort() function is implemented using the Timsort algorithm, which has a worst-case space complexity of O(n)

# Base Idea (One line)

1. Sort or Set

# Explanation

[Reference]

[Find the Duplicate Number - LeetCode](https://leetcode.com/problems/find-the-duplicate-number/solution/)

[https://leetcode.com/problems/find-the-duplicate-number/discuss/2346451/Python-O(n)-time-O(1)-space-easy-solution](https://leetcode.com/problems/find-the-duplicate-number/discuss/2346451/Python-O(n)-time-O(1)-space-easy-solution)

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:   # Time: O(n) and Space: O(1)
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]
```