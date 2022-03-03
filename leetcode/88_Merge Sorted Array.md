# 88. Merge Sorted Array

Acceptance: 0.434
Difficulty: Easy
Frequency: 0.7091
Skills: Array, Sorting, Two Pointers
Solved: February 28, 2022

# Description

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be *stored inside the array* `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

**Example 1:**

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

```

**Example 2:**

```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

```

**Example 3:**

```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

```

**Constraints:**

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `109 <= nums1[i], nums2[j] <= 109`

# Solutions

### Python

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # O((m+n)log(m+n)) solution
        j = 0
        for i in range(m, m+n):
            if nums1[i] == 0:
                nums1[i] = nums2[j]
                j += 1
        nums1.sort() #O((m+n)log(m+n))
```

> Runtime: 48 ms, faster than 62.66% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14 MB, less than 50.83% of Python3 online submissions for Merge Sorted Array.
> 

### Complexity Analysis

- Time complexity : O((m+n)log(m+n)), where m is the length of nums1, n is the length of nums2
- Space complexity : O(1), since we don’t use any additional memory

## Python Sol2 - Two Pointers

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # O(m+n)
        i = 0
        j = 0
        total_nums = []
        if m == 0:
            print('h')
            print(nums1)
            print(nums2)
            nums1 = nums2
            print(nums1)
        else:
            while i < m or j < n:
                if i >=m or (j < n and nums1[i] > nums2[j]):
                    total_nums.append(nums2[j])
                    j += 1
                elif nums1[i] <= nums2[j]:
                    total_nums.append(nums1[i])
                    i += 1
            nums1 = total_nums
            print(total_nums)
```

# Base Idea (One line)

1. nums1의 m 뒷부분에 nums2를 붙이고 sort
2. 뒷 부분부터 채워서 array 중간 삽입 상황을 피한다

# Explanation

[Reference]

[Merge Sorted Array - LeetCode](https://leetcode.com/problems/merge-sorted-array/solution/)

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # O(m+n)
        p1 = m - 1
        p2 = n - 1
        
        for p in range(m+n-1,-1, -1):
            if p1 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            elif p2 >= 0 and nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
```