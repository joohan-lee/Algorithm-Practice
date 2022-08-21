# 1143. Longest Common Subsequence

Acceptance: 58.9%
Difficulty: Medium
Frequency: 53.17%
Skills: Dynamic Programming, String
Solved: August 20, 2022

# Description

Given two strings `text1` and `text2`, return *the length of their longest **common subsequence**.* If there is no **common subsequence**, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both strings.

**Example 1:**

```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

```

**Example 2:**

```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

```

**Example 3:**

```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

```

**Constraints:**

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

# Solutions

### Python

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m) for _ in range(n)]
        
        for i in range(n):
            if text2[0] == text1[i]:
                for k in range(i,n):
                    dp[k][0] = 1
                break
        for j in range(m):
            if text1[0] == text2[j]:
                for k in range(j,m):
                    dp[0][k] = 1
                break
       
        
        for i in range(1,n):
            for j in range(1,m):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(dp)
        return dp[n-1][m-1]
```

> Runtime: 668 ms, faster than 53.41% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 22.1 MB, less than 69.17% of Python3 online submissions for Longest Common Subsequence.
> 

### Complexity Analysis

- Time complexity : O(MN)
- Space complexity : O(MN)

# Base Idea (One line)

1. dp[i][j] represents the longest common subsequence of text1[0…i] and text2[0…j]

# Explanation

[Reference]

[](https://leetcode.com/problems/longest-common-subsequence/solution/)