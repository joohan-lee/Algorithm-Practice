# 26. Remove Duplicates from Sorted Array

Acceptance: 49.5%
Difficulty: Easy
Frequency: 65.84%
Skills: Array, Two Pointers
Solved: July 12, 2022

# Description

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` *after placing the final result in the first* `k` *slots of* `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

**Custom Judge:**

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

```

If all assertions pass, then your solution will be **accepted**.

**Example 1:**

```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

**Example 2:**

```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

**Constraints:**

- `1 <= nums.length <= 3 * 104`
- `100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing** order.

# Solutions

### Python

Dictionary

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dict = {}
        idx = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] not in dict:
                nums[idx] = nums[i]
                dict[nums[i]] = 1
                cnt += 1
                idx += 1
        for i in range(len(nums) - cnt):
            nums.pop()
```

> Runtime: 85 ms, faster than 97.59% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 60.57% of Python3 online submissions for Remove Duplicates from Sorted Array.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

### Python

Two pointers

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1
```

Runtime: 119 ms, faster than 71.30% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 16.09% of Python3 online submissions for Remove Duplicates from Sorted Array.

Time Complexity: O(n)

Space Complexity: O(1)

# Base Idea (One line)

1. dictionary
2. two points

# Explanation

[Reference]

[Remove Duplicates from Sorted Array - LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/)