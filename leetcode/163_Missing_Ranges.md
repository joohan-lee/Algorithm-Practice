# 163. Missing Ranges

Acceptance: 31.8%
Difficulty: Easy
Frequency: 45.55%
Skills: Array
Solved: September 13, 2022

# Description

You are given an inclusive range `[lower, upper]` and a **sorted unique** integer array `nums`, where all elements are in the inclusive range.

A number `x` is considered **missing** if `x` is in the range `[lower, upper]` and `x` is not in `nums`.

Return *the **smallest sorted** list of ranges that **cover every missing number exactly***. That is, no element of `nums` is in any of the ranges, and each missing number is in one of the ranges.

Each range `[a,b]` in the list should be output as:

- `"a->b"` if `a != b`
- `"a"` if `a == b`

**Example 1:**

```
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"

```

**Example 2:**

```
Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.

```

**Constraints:**

- `109 <= lower <= upper <= 109`
- `0 <= nums.length <= 100`
- `lower <= nums[i] <= upper`
- All the values of `nums` are **unique**.

# Solutions

### Python

```python
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        missing = []
        prev_num = lower - 1
        for i in range(len(nums) + 1):
            curr_num = nums[i] if i < len(nums) else upper + 1
            gap = curr_num - prev_num
            if gap == 2:
                missing.append(str(prev_num + 1))
            elif gap > 2:
                missing.append(str(prev_num+1) + "->" + str(curr_num-1))
            
            prev_num = curr_num
        
        
        return missing
```

> Runtime: 51 ms, faster than 41.14% of Python3 online submissions for Missing Ranges.
Memory Usage: 13.8 MB, less than 84.44% of Python3 online submissions for Missing Ranges.
> 

### Complexity Analysis

- Time complexity : O(N) where N is the length of nums
- Space complexity : O(1)

# Base Idea (One line)

1. When `nums[i] - nums[i-1] == 1`, we know that there are no missing elements between `nums[i-1]` and `nums[i]`. When `nums[i] - nums[i-1] > 1`, we know that the range of elements, `[nums[i-1] + 1, nums[i] - 1]`, is missing.

# Explanation

[Reference]

[Account Login - LeetCode](https://leetcode.com/problems/missing-ranges/solution/)