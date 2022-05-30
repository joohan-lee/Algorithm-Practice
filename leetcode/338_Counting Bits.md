# 338. Counting Bits

Acceptance: 74.4%
Difficulty: Easy
Frequency: 54.00%
Skills: Dynamic Programming, bit manipulation
Solved: May 29, 2022

# Description

Given an integer `n`, return *an array* `ans` *of length* `n + 1` *such that for each* `i` **(`0 <= i <= n`)*,* `ans[i]` *is the **number of*** `1`***'s** in the binary representation of* `i`.

**Example 1:**

```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

```

**Example 2:**

```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

```

**Constraints:**

- `0 <= n <= 105`

**Follow up:**

- It is very easy to come up with a solution with a runtime of `O(n log n)`. Can you do it in linear time `O(n)` and possibly in a single pass?
- Can you do it without using any built-in function (i.e., like `__builtin_popcount` in C++)?

# Solutions

### Python

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        # DP + Least Significant Bit
        # P(x) = P(x/2) + (x mod 2)
        ans = [0] * (n+1)
        for x in range(1,n+1):
            # x//2 == x>>1 and x%2 == x&1
            ans[x] = ans[x>>1] + (x&1)
        return ans
```

> Runtime: 161 ms, faster than 33.30% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 29.14% of Python3 online submissions for Counting Bits.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(1), since the output array does not count towards the space complexity.

# Base Idea (One line)

1. i & 1 == i % 2
2. Improve algorithm using DP

# Explanation

[Reference]

[Counting Bits - LeetCode](https://leetcode.com/problems/counting-bits/solution/)