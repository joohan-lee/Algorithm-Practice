# 387. First Unique Character in a String

Acceptance: 58.9%
Difficulty: Easy
Frequency: 77.79%
Skills: Counting, Hash Table, Queue, String
Solved: October 31, 2022
다시풀기: Once

# Description

Given a string `s`, *find the first non-repeating character in it and return its index*. If it does not exist, return `-1`.

**Example 1:**

```
Input: s = "leetcode"
Output: 0

```

**Example 2:**

```
Input: s = "loveleetcode"
Output: 2

```

**Example 3:**

```
Input: s = "aabb"
Output: -1

```

**Constraints:**

- `1 <= s.length <= 105`
- `s` consists of only lowercase English letters.

# Solutions

### Python

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        visited = {}
        for i, ch in enumerate(s):
            if ch in visited:
                visited[ch] += 1
            else:
                visited[ch] = 1
        
        for i,ch in enumerate(s):
            if visited[ch] == 1:
                return i
        return -1
```

> Runtime: 133 ms, faster than 83.21% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.2 MB, less than 17.98% of Python3 online submissions for First Unique Character in a String.
> 

### Complexity Analysis

- Time complexity : O(N)
- Space complexity : O(1)

# Base Idea (One line)

1. Using a hash map, store the number of each letter.

# Explanation

[Reference]

[First Unique Character in a String - LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/solution/)