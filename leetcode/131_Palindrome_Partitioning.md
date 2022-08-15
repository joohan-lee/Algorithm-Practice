# 131. Palindrome Partitioning

Acceptance: 61.4%
Difficulty: Medium
Frequency: 63.56%
Skills: Backtracking, Dynamic Programming, String
Solved: August 13, 2022
다시풀기: Required

# Description

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return all possible palindrome partitioning of `s`.

A **palindrome** string is a string that reads the same backward as forward.

**Example 1:**

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

```

**Example 2:**

```
Input: s = "a"
Output: [["a"]]

```

**Constraints:**

- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

# Solutions

### Python

### 1. Backtracking

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(ps):
            start = 0
            end = len(ps) - 1
            
            while start < end:
                if ps[start] != ps[end]:
                    return False
                start += 1
                end -= 1
            
            return True
                
        def dfs(start, s, currentList):
            if start >= len(s):
                return result.append(list(currentList))
            
            for end in range(start, len(s)):
                substr = s[start:end+1]
                if isPalindrome(substr):
                    currentList.append(substr)
                    dfs(end + 1, s, currentList)
                    currentList.pop()
                    
            
        
        
        result = []
        dfs(0, s, [])
        return result
```

> Runtime: 1610 ms, faster than 5.02% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 30.3 MB, less than 43.41% of Python3 online submissions for Palindrome Partitioning.
> 

### Complexity Analysis

- Time complexity : O(N*2^N), where N is the length of string s. This is the worst-case time complexity when all the possible substrings are palindrome.
- Space complexity : O(N) This place will be used to store the recursion stack. For s= aaa, the maximum depth of the recursive call stack is 3 which is equivalent to N.

### 2. Backtracking with DP

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
                
        def dfs(start, s, currentList):
            if start >= len(s):
                return result.append(list(currentList))
            
            for end in range(start, len(s)):
                substr = s[start:end+1]
                if (s[start] == s[end] and (end - start <=2 or dp[start+1][end-1])):
                    currentList.append(substr)
                    dp[start][end] = True
                    dfs(end + 1, s, currentList)
                    currentList.pop()
                    
            
        n = len(s)
        result = []
        dp = [[False] * n for _ in range(n)]
        dfs(0, s, [])
        return result
```

> Runtime: 756 ms, faster than 80.27% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 30.4 MB, less than 43.41% of Python3 online submissions for Palindrome Partitioning.
> 

### Complexity Analysis

- Time complexity : O(N*2^N)
- Space complexity : O(N*N)

# Base Idea (One line)

1. Check all possible substrings with backtracking.
2. While checking substring is a palindrome or not, there are overlapping subproblems, so use DP.

# Explanation

[Reference]

[Palindrome Partitioning - LeetCode](https://leetcode.com/problems/palindrome-partitioning/solution/)