# 242. Valid Anagram

Acceptance: 62.5%
Difficulty: Easy
Frequency: 74.45%
Skills: Hash Table, Sorting, String
Solved: August 24, 2022

# Description

Given two strings `s` and `t`, return `true` *if* `t` *is an anagram of* `s`*, and* `false` *otherwise*.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

```
Input: s = "anagram", t = "nagaram"
Output: true

```

**Example 2:**

```
Input: s = "rat", t = "car"
Output: false

```

**Constraints:**

- `1 <= s.length, t.length <= 5 * 104`
- `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# Solutions

### Python

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        for ch in s:
            if ch not in hash_s:
                hash_s[ch] = 1
            else:
                hash_s[ch] += 1
        
        hash_t = {}
        for ch in t:
            if ch not in hash_t:
                hash_t[ch] = 1
            else:
                hash_t[ch] += 1
            
        return hash_s == hash_t
```

> Runtime: 59 ms, faster than 79.32% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.3 MB, less than 97.11% of Python3 online submissions for Valid Anagram.
> 

### Complexity Analysis

- Time complexity : O(M+N), where m and n are the length of each string
- Space complexity : O(M+N)

We don’t actually make a hash table because the lower characters are always 26. We can just create a list with 26 indices sequentially from a to z, then count the characters in the string, and then store the number of each character into the list.

# Base Idea (One line)

1. Sort both strings and compare them whether they are same or not.
2. Count all characters using hash table and compare both hash tables have same items.

# Explanation

[Reference]

[Valid Anagram - LeetCode](https://leetcode.com/problems/valid-anagram/solution/)