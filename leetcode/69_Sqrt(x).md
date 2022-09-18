# 69. Sqrt(x)

Acceptance: 36.9%
Difficulty: Easy
Frequency: 64.90%
Skills: Binary Search, Math
Solved: September 17, 2022

# Description

Given a non-negative integer `x`, compute and return *the square root of* `x`.

Since the return type is an integer, the decimal digits are **truncated**, and only **the integer part** of the result is returned.

**Note:** You are not allowed to use any built-in exponent function or operator, such as `pow(x, 0.5)` or `x ** 0.5`.

**Example 1:**

```
Input: x = 4
Output: 2

```

**Example 2:**

```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
```

**Constraints:**

- `0 <= x <= 231 - 1`

# Solutions

### Python

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x+1):
            if i * i == x:
                return i
            elif i*i > x:
                return i - 1
```

> Runtime: 3828 ms, faster than 11.00% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.7 MB, less than 95.78% of Python3 online submissions for Sqrt(x).
> 

### Complexity Analysis

- Time complexity : O(x)
- Space complexity : O(1)

### Python - Binary Search

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        lo = 2
        hi = x // 2
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return hi
```

Runtime: 45 ms, faster than 84.46% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.9 MB, less than 56.48% of Python3 online submissions for Sqrt(x).

### Complexity Analysis

- Time complexity : O(logN)
- Space complexity : O(1)

# Base Idea (One line)

1. Since 0 to x is sorted, we can consider binary search.

# Explanation

[Reference]

[Sqrt(x) - LeetCode](https://leetcode.com/problems/sqrtx/solution/)