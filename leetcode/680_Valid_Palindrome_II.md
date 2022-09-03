# 680. Valid Palindrome II

Acceptance: 39.4%
Difficulty: Easy
Frequency: 92.67%
Skills: Greedy, String, Two Pointers
Solved: September 2, 2022

# Description

Given a string `s`, return `true` *if the* `s` *can be palindrome after deleting **at most one** character from it*.

**Example 1:**

```
Input: s = "aba"
Output: true

```

**Example 2:**

```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

```

**Example 3:**

```
Input: s = "abc"
Output: false

```

**Constraints:**

- `1 <= s.length <= 105`
- `s` consists of lowercase English letters.

# Solutions

### Python

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1
        
        while lo <= hi:
            if s[lo] != s[hi]:
                left = s[lo:hi]
                right = s[lo+1:hi+1]
                return left == left[::-1] or right == right[::-1]
            lo += 1
            hi -= 1
        
        return True
```

> Runtime: 106 ms, faster than 93.55% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 14.5 MB, less than 89.83% of Python3 online submissions for Valid Palindrome II.
> 

### Complexity Analysis

- Time complexity : O(N), it takes O(N/2) for the while loop and O(N) when we found mismatch, to compare remaining characters
- Space complexity : O(N) for left and right.

# Base Idea (One line)

1. Two Pointers and check twice by deleting each mismatching character

# Explanation

[Reference]

[Valid Palindrome II - LeetCode](https://leetcode.com/problems/valid-palindrome-ii/solution/)