# 283. Move Zeroes

Acceptance: 60.8%
Difficulty: Easy
Frequency: 71.44%
Skills: Array, Two Pointers
Solved: May 29, 2022

# Description

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

**Example 1:**

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

**Example 2:**

```
Input: nums = [0]
Output: [0]

```

**Constraints:**

- `1 <= nums.length <= 104`
- `231 <= nums[i] <= 231 - 1`

**Follow up:**

Could you minimize the total number of operations done?

# Solutions

### Python

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0
        cur = 0
        while cur < len(nums):
            if nums[cur] != 0:
                nums[lastNonZero], nums[cur] = nums[cur], nums[lastNonZero]
                lastNonZero += 1
            cur += 1
```

> Runtime: 327 ms, faster than 25.15% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.5 MB, less than 65.09% of Python3 online submissions for Move Zeroes.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(1)

# Base Idea (One line)

1. Using two pointers. One points to the index of non-zero element, the other just iterates all.

# Explanation

[Reference]

Similar, but another way

```python
void moveZeroes(vector<int>& nums) {
    int lastNonZeroFoundAt = 0;
    // If the current element is not 0, then we need to
    // append it just in front of last non 0 element we found. 
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 0) {
            nums[lastNonZeroFoundAt++] = nums[i];
        }
    }
 	// After we have finished processing new elements,
 	// all the non-zero elements are already at beginning of array.
 	// We just need to fill remaining array with 0's.
    for (int i = lastNonZeroFoundAt; i < nums.size(); i++) {
        nums[i] = 0;
    }
}
```

[Move Zeroes - LeetCode](https://leetcode.com/problems/move-zeroes/solution/)