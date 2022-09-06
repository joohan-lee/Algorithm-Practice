# 55. Jump Game

Acceptance: 38.3%
Difficulty: Medium
Frequency: 73.93%
Skills: Array, Dynamic Programming, Greedy
Solved: September 5, 2022
다시풀기: Required

# Description

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` *if you can reach the last index, or* `false` *otherwise*.

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

```

**Example 2:**

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

```

**Constraints:**

- `1 <= nums.length <= 104`
- `0 <= nums[i] <= 105`

# Solutions

### Python

### 1. Backtracking

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def canJumpFromPosition(position, nums):
            if position == len(nums) - 1:
                return True

            furthestJump = min(position + nums[position], len(nums) - 1)
            for i in range(position + 1, furthestJump+1):
                if canJumpFromPosition(i, nums):
                    return True
        
        return canJumpFromPosition(0,nums)
```

> Runtime: Time Limit Exceed
Memory Usage:
> 

### Complexity Analysis

- Time complexity : O(2^n)
- Space complexity : O(n)

### 2. DP Top Down

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def canJumpFromPosition(position, nums):
            if memo[position] != 'U':
                return True if memo[position] == 'G' else False

            furthestJump = min(position + nums[position], len(nums) - 1)
            for i in range(position + 1, furthestJump+1):
                if canJumpFromPosition(i, nums):
                    memo[position] = 'G'
                    return True
            
            memo[position] = 'B'
            return False
        
        
        # 'U': Unknow, 'G': Good, 'B': Bad
        memo = ['U' for _ in range(len(nums))]
        memo[len(nums)-1] = 'G'
        
        return canJumpFromPosition(0, nums)
```

O(n^2) time, O(n) space

### 3. DP Bottom up

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 'U': Unknow, 'G': Good, 'B': Bad
        memo = ['U' for _ in range(len(nums))]
        memo[len(nums)-1] = 'G'
        
        i = len(nums) - 2
        while i >= 0:
            furthestJump = min(i + nums[i], len(nums) - 1)
            for j in range(i+1, furthestJump + 1):
                if memo[j] == 'G':
                    memo[i] = 'G'
                    break
            i -= 1
        
        
        
        return True if memo[0] == 'G' else False
```

> Runtime: 8040 ms, faster than 5.00% of Python3 online submissions for Jump Game.
Memory Usage: 15.3 MB, less than 49.33% of Python3 online submissions for Jump Game.
> 

O(n^2) time, O(n) space

### 4. Greedy

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 'U': Unknow, 'G': Good, 'B': Bad
        memo = ['U' for _ in range(len(nums))]
        memo[len(nums)-1] = 'G'
        
        i = len(nums) - 2
        lastpos = len(nums) - 1
        while i >= 0:
            if i + nums[i] >= lastpos:
                lastpos = i
            i -= 1
        
        
        
        return True if lastpos == 0 else False
```

Runtime: 762 ms, faster than 51.30% of Python3 online submissions for Jump Game.
Memory Usage: 15.2 MB, less than 49.33% of Python3 online submissions for Jump Game.

O(n), O(1)

# Base Idea (One line)

1. Iterate through all cases using Backtracking and find repeated calculations, and then use DP.
2. We don't even need DP and we can use Greedy which solves the problem faster with low space

# Explanation

[Reference]

[Jump Game - LeetCode](https://leetcode.com/problems/jump-game/solution/)