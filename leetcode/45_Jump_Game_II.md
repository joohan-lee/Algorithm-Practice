# 45. Jump Game II

Acceptance: 38.4%
Difficulty: Medium
Frequency: 74.01%
Skills: Array, Dynamic Programming, Greedy
Solved: September 19, 2022
다시풀기: Required

# Description

Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

```

**Example 2:**

```
Input: nums = [2,3,0,1,4]
Output: 2

```

**Constraints:**

- `1 <= nums.length <= 104`
- `0 <= nums[i] <= 1000`

# Solutions

### Python

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currentJumpEnd = 0
        farthest = 0
        path = []
        for i in range(len(nums)-1):
            # we continuously(at every index) find the how far we can reach in the current jump
            # farthest = max(farthest, i + nums[i])
            if i + nums[i] > farthest:
                farthest = i + nums[i]
                # path.append(i)
            # if we have come to the end of the current jump,
            # we need to make another jump
            if i == currentJumpEnd:
                jumps += 1
                currentJumpEnd = farthest
        # print(path)
        return jumps
```

> Runtime: 299 ms, faster than 40.88% of Python3 online submissions for Jump Game II.
Memory Usage: 15.2 MB, less than 21.76% of Python3 online submissions for Jump Game II.
> 

### Complexity Analysis

- Time complexity : O(N)
- Space complexity : O(1)

# Base Idea (One line)

1. Since we can always reach the last index, we can just jump as farthest as possible.

# Explanation

[Reference]

[Jump Game II - LeetCode](https://leetcode.com/problems/jump-game-ii/solution/)