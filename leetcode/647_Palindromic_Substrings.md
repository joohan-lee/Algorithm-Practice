# 647. Palindromic Substrings

Acceptance: 66.0%
Difficulty: Medium
Frequency: 66.13%
Skills: Dynamic Programming, String
Solved: August 9, 2022

# Description

Given a string `s`, return *the number of **palindromic substrings** in it*.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

**Example 1:**

```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

```

**Example 2:**

```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

```

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

# Solutions

### Python

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        ans = 0
        # base case (when the length of substring is 1 or 2)
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                    ans += 1
                if j == i+1 and s[i] == s[j]:
                    dp[i][j] = True
                    ans += 1
        
        # overlapping sub-problems (the length of substrings are higher than 2)
        for l in range(3, n+1):
            i = 0
            for j in range(i + l -1, n):
                if s[i] == s[j] and dp[i+1][j-1] == True:
                    dp[i][j] = True
                if dp[i][j]:
                    ans += 1
                i += 1
        
        
        return ans
```

> Runtime: 747 ms, faster than 12.27% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 22.5 MB, less than 13.93% of Python3 online submissions for Palindromic Substrings.
> 

### Complexity Analysis

- Time complexity : O(N^2) for input string of length N.
- Space complexity : O(N^2)

# Base Idea (One line)

1. DP(i,j) = True or False(whether the substring composed of i-th to the j-th characters of the input string is a palindrome or not)

# Explanation

[Reference]

[Palindromic Substrings - LeetCode](https://leetcode.com/problems/palindromic-substrings/solution/)