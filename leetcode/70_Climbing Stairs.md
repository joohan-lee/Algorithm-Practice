# 70. Climbing Stairs

Acceptance: 51.1%
Difficulty: Easy
Frequency: 73.59%
Skills: Dynamic Programming, Math, Memoization
Solved: May 17, 2022

# Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

```

**Example 2:**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

```

**Constraints:**

- `1 <= n <= 45`

# Solutions

### Python

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # n = step(i-1) + 1 or step(i-2) + 2
        # since there are only two ways for the last step to get the top.
        
        # 사실상 1step 부터 시작하므로 index 3까지 initilze해줘야 step2까지 되는 것임.
        opt = [0, 1, 2]
        
        
        for i in range(3, n+1):
            opt.append((opt[i-1]) + (opt[i-2]))
        
        return opt[n]
```

> Runtime: 46 ms, faster than 35.25% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.9 MB, less than 58.36% of Python3 online submissions for Climbing Stairs.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n) to store the values of optimal solutions

# Base Idea (One line)

1. Dynamic Programming
2. or Recursion with memoization

# Explanation

[Reference]

[Climbing Stairs - LeetCode](https://leetcode.com/problems/climbing-stairs/solution/)

```python
# Recursion with memoization version

class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = [0 for _ in range(n+1)]
        def climb(self, i, n):
            if i > n:
                return 0
            if i == n:
                return 1
            if self.memo[i] != 0:
                return self.memo[i]
            
            self.memo[i] = climb(self, i+1, n) + climb(self, i+2, n)
            return self.memo[i]
        return climb(self, 0,n)
```

Runtime: **33 ms**

Memory Usage: **13.9 MB**