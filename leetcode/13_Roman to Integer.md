# 13. Roman to Integer

Acceptance: 57.9%
Difficulty: Easy
Frequency: 88.61%
Skills: Hash Table, Math, String
Solved: April 11, 2022

# Description

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
SymbolValue
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two one's added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

**Example 1:**

```
Input: s = "III"
Output: 3
Explanation: III = 3.

```

**Example 2:**

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

```

**Example 3:**

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

```

**Constraints:**

- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

# Solutions

### Python

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        total = 0
        i = 0
        while i < len(s):
            cur = int(values[s[i]])
            if i < len(s)-1:
                next = int(values[s[i+1]])
                # 다음 글자보다 현재 글자가 크거나 같으면 그냥 덧셈
                if next <= cur:
                    total += cur
                    i += 1
                # 다음 글자가 현재 글자보다 크면 다음 글자에서 현재 글자를 뺀 만큼 더함
                else:
                    total += (next - cur)
                    i += 2
            else:
                total += cur
                i += 1
       
        return total
```

> Runtime: 63 ms, faster than 60.83% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.9 MB, less than 80.61% of Python3 online submissions for Roman to Integer.
> 

### Complexity Analysis

- Time complexity : O(1), since there is a finite set of roman numerals, the maximum number possible number can be `3999`
- Space complexity : O(1)

# Base Idea (One line)

1. 뒤 숫자보다 앞 숫자가 작으면 (뒤 숫자 - 앞 숫자)를 더해주어 계산한다는 규칙 발견
2. Hash Table의 유연한 사용

# Explanation

[Reference]

[Roman to Integer - LeetCode](https://leetcode.com/problems/roman-to-integer/solution/)

```python
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += values[s[i]]
                i += 1
        return total
```