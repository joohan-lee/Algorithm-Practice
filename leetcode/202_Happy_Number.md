# 202. Happy Number

Acceptance: 54.3%
Difficulty: Easy
Frequency: 66.89%
Skills: Hash Table, Math, Two Pointers
Solved: October 19, 2022

# Description

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process **ends in 1** are happy.

Return `true` *if* `n` *is a happy number, and* `false` *if not*.

**Example 1:**

```
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

```

**Example 2:**

```
Input: n = 2
Output: false

```

**Constraints:**

- `1 <= n <= 231 - 1`

# Solutions

### Python

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()
        while n != 1:
            if n in hash_set:
                return False
            else:
                hash_set.add(n)
            str_n = str(n)
            curr_sum = 0
            for i in range(len(str_n)):
                curr_sum += int(str_n[i]) ** 2
            
            n = curr_sum
        
        return True
```

> Runtime: 67 ms, faster than 40.31% of Python3 online submissions for Happy Number.
Memory Usage: 13.8 MB, less than 61.02% of Python3 online submissions for Happy Number.
> 

### Complexity Analysis

- Time complexity : O(logn)
- Space complexity : O(logn)

Refer [here](https://leetcode.com/problems/happy-number/solution/)

# Base Idea (One line)

1. If same number appears twice, it means there is a cycle. We can detect it using hash set.

# Explanation

[Reference]

[Happy Number - LeetCode](https://leetcode.com/problems/happy-number/solution/)