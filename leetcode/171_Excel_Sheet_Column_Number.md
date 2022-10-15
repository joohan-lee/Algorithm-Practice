# 171. Excel Sheet Column Number

Acceptance: 61.3%
Difficulty: Easy
Frequency: 50.40%
Skills: ASCII, Math, String
Solved: October 15, 2022

# Description

Given a string `columnTitle` that represents the column title as appears in an Excel sheet, return *its corresponding column number*.

For example:

```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

```

**Example 1:**

```
Input: columnTitle = "A"
Output: 1

```

**Example 2:**

```
Input: columnTitle = "AB"
Output: 28

```

**Example 3:**

```
Input: columnTitle = "ZY"
Output: 701

```

**Constraints:**

- `1 <= columnTitle.length <= 7`
- `columnTitle` consists only of uppercase English letters.
- `columnTitle` is in the range `["A", "FXSHRXW"]`.

# Solutions

### Python

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ch = 'A'
        ch_map = {}
        while ord(ch) <= ord('Z'):
            ch_map[ch] = ord(ch) - ord('A') + 1
            ch = chr(ord(ch)+1)
        
        res = 0
        columnTitle_length = len(columnTitle)
        for i in range(columnTitle_length-1, -1, -1):
            col = columnTitle[i]
            res += ch_map[col] * (26 ** (columnTitle_length-i - 1))
            
        return res
```

> Runtime: 77 ms, faster than 6.81% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.9 MB, less than 10.95% of Python3 online submissions for Excel Sheet Column Number.
> 

### Complexity Analysis

- Time complexity : O(N), where N is the length of the string.
- Space complexity : O(1), the number of alphabet is constant(26)

# Base Idea (One line)

1. Using ASCII code and converting base 26 numbers to decimal numbers.

# Explanation

[Reference]

[Excel Sheet Column Number - LeetCode](https://leetcode.com/problems/excel-sheet-column-number/solution/)