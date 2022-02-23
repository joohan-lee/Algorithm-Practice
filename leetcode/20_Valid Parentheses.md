# 20. Valid Parentheses

Acceptance: 0.406
Difficulty: Easy
Frequency: 0.9562
Skills: Stack, String
Solved: February 23, 2022

# Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

**Example 1:**

```
Input: s = "()"
Output: true

```

**Example 2:**

```
Input: s = "()[]{}"
Output: true

```

**Example 3:**

```
Input: s = "(]"
Output: false

```

**Constraints:**

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

# Solutions

### Python

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == "{":
                stack.append(ch)
            elif ch == "[":
                stack.append(ch)
            else:
                if stack == []:
                    return False
                top = stack.pop()
                if ch == ")" and top != "(":
                    return False
                elif ch == "}" and top != "{":
                    return False
                elif ch == "]" and top != "[":
                    return False
        return True if stack ==[] else False
```

> Runtime: 24 ms, faster than 98.57% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14 MB, less than 55.84% of Python3 online submissions for Valid Parentheses.
> 

### Complexity Analysis

- Time complexity : O(n), where n is the length of s.
- Space complexity : O(n), where n is the length of s, because I use additional memory, stack.

# Base Idea (One line)

1. Stack
2. Replace all parentheses with '', if empty then True, else False

# Explanation

[Reference]

[Valid Parentheses - LeetCode](https://leetcode.com/problems/valid-parentheses/solution/)

There is another solution which is interesting.

```python
def isValid(self, s):
         # python replace
         n = len(s)
         if n == 0:
             return True
    
         if n % 2 != 0:
             return False
			    
				#If it is valid, all parentheses must be replaced,
				# since all open brackets must be closed by the same type of brackets.
         while '()' in s or '{}' in s or '[]' in s:
             s = s.replace('{}', '').replace('()', '').replace('[]', '')
		
         if s == '':
             return True
         else:
             return False
```

reference : [https://github.com/qiyuangong/leetcode/blob/master/python/020_Valid_Parentheses.py](https://github.com/qiyuangong/leetcode/blob/master/python/020_Valid_Parentheses.py)