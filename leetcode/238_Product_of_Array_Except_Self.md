# 238. Product of Array Except Self

Acceptance: 64.4%
Difficulty: Medium
Frequency: 81.25%
Skills: Array, Prefix Sum
Solved: August 10, 2022

# Description

Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

```

**Example 2:**

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

```

**Constraints:**

- `2 <= nums.length <= 105`
- `30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

# Solutions

### Python

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 현 index를 뺀 product of all elements는 
        # 현 인덱스 좌를 모두 곱한 값 * 우를 모두 곱한 값과 같다.
        # 즉, O(2n)으로 해결 가능.
        
        length = len(nums)
        
        L = [0] * length
        R = [0] * length
        ans = [0] * length
        
        L[0] = 1
        for i in range(1, length):
            L[i] = L[i-1] * nums[i-1]
            
        R[length-1] = 1
        for i in range(length -2, -1, -1):
            R[i] = nums[i+1] * R[i+1]
        
        for i in range(length):
            ans[i] = L[i] * R[i]
        
        return ans
```

> Runtime: 387 ms, faster than 40.45% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 22.4 MB, less than 18.28% of Python3 online submissions for Product of Array Except Self.
> 

### Complexity Analysis

- Time complexity : O(N) where N represents the number of elements in the input array.
- Space complexity : O(N)

# Base Idea (One line)

1. productExceptSelf[i] = (productLeftSide of i) * (productRightSide of i)

# Explanation

[Reference]

[Product of Array Except Self - LeetCode](https://leetcode.com/problems/product-of-array-except-self/solution/)