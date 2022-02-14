# 1614. Maximum Nesting Depth of the Parentheses

Acceptance: 0.83
Difficulty: Easy
Skills: Stack
Solved: November 2, 2021

# Description

A string is a **valid parentheses string** (denoted **VPS**) if it meets one of the following:

- It is an empty string `""`, or a single character not equal to `"("` or `")"`,
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are **VPS**'s, or
- It can be written as `(A)`, where `A` is a **VPS**.

We can similarly define the **nesting depth** `depth(S)` of any VPS `S` as follows:

- `depth("") = 0`
- `depth(C) = 0`, where `C` is a string with a single character not equal to `"("` or `")"`.
- `depth(A + B) = max(depth(A), depth(B))`, where `A` and `B` are **VPS**'s.
- `depth("(" + A + ")") = 1 + depth(A)`, where `A` is a **VPS**.

For example, `""`, `"()()"`, and `"()(()())"` are **VPS**'s (with nesting depths 0, 1, and 2), and `")("` and `"(()"` are not **VPS**'s.

Given a **VPS** represented as string `s`, return *the **nesting depth** of* `s`.

**Example 1:**

```
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

```

**Example 2:**

```
Input: s = "(1)+((2))+(((3)))"
Output: 3

```

**Example 3:**

```
Input: s = "1+(2*3)/(2-1)"
Output: 1

```

**Example 4:**

```
Input: s = "1"
Output: 0

```

**Constraints:**

- `1 <= s.length <= 100`
- `s` consists of digits `0-9` and characters `'+'`, `'-'`, `'*'`, `'/'`, `'('`, and `')'`.
- It is guaranteed that parentheses expression `s` is a **VPS**.

# Solutions

Provide possible solutions in common languages to this problem.

### Python

```python
class Solution:
    def maxDepth(self, s: str) -> int:
        #공백 or single이면 0
        if s == "" or len(s) == 1:
            return 0
        
        #"("를 만나면 stack에 삽입, ")"를 만나면 stack에서 "("를 pop 그리고 stack의 최대 size 였을 때가 nesting depth
        stack = []
        depth = 0
        max_depth = 0
        for ch in s:
            if ch == "(":
                stack.append(ch)
                depth += 1
                max_depth = max(depth, max_depth)
            elif ch == ")":
                stack.pop()
                depth -= 1
        return max_depth
```

> Runtime: **32 ms**
Memory Usage: **14.2 MB**
> 

# Complexity Analysis

- Time complexity : O(N), where N is the length of string.
- Space complexity : *O*(*n*), where n is the length of string. Since we use additional memory, stack. 사실 정확히는 O("("의 개수) 일 것이다. 하지만 이런 경우 어떻게 말해야할까,,?

# 해설

해설 참고자료