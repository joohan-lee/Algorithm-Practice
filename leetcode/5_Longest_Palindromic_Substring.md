# 5. Longest Palindromic Substring

Acceptance: 32.3%
Difficulty: Medium
Frequency: 94.75%
Skills: Dynamic Programming, String
Solved: August 25, 2022

# Description

Given a string `s`, return *the longest palindromic substring* in `s`.

**Example 1:**

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

```

**Example 2:**

```
Input: s = "cbbd"
Output: "bb"

```

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

# Solutions

### Python

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # OPT[i,j] = the length of the longest palindromic substring of S[i,...,j]
        # if S[i] == S[j], then OPT[i,j] = OPT[i+1,j-1] + 2
        # if S[i] != S[j], then OPT[i,j] = max(OPT(i,j-1),OPT(i+1,j))
        # 위는 다른 경우.(연속되지 않아도 되는 경우)
        
        n = len(s)
        
        opt = [[False] * n for _ in range(n)]
        max_case = (0,0)
        
        # We will care i <= j because opt(i,j) = whether s[i...j] is palindrom or not
        # base case
        # 1. opt(i,i) = True
        for i in range(n):
            opt[i][i] = True
        # 2. opt(i,i+1) = True if s[i] == s[i+1]
        for i in range(n-1):
            if s[i] == s[i+1]:
                opt[i][i+1] = True
                max_case = (i,i+1)
        
        # bottom-up , fill up diagonally
        for gap in range(2, n+1): # i + gap == j
            i = 0
            for j in range(i+gap, n):
                if opt[i+1][j-1] == True and s[i] == s[j]:
                    opt[i][j] = True
                    if j - i > max_case[1] - max_case[0]:
                        max_case = (i,j)
                i += 1
            
        return s[max_case[0]:max_case[1]+1]
```

> Runtime: 5192 ms, faster than 14.15% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 22 MB, less than 5.46% of Python3 online submissions for Longest Palindromic Substring.
> 

### Complexity Analysis

- Time complexity : O(n^2)
- Space complexity : O(n^2)

# Base Idea (One line)

1. 2-dimensional DP. opt(i,j) = whether s[i:j+1] is palindrome or not.

# Explanation

[Reference]

[Longest Palindromic Substring - LeetCode](https://leetcode.com/problems/longest-palindromic-substring/solution/)