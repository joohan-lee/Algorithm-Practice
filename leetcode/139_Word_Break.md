# 139. Word Break

Acceptance: 45.3%
Difficulty: Medium
Frequency: 77.51%
Skills: Dynamic Programming, Hash Table, Memoization, String, Trie
Solved: September 26, 2022

# Description

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

**Example 1:**

```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

```

**Example 2:**

```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

```

**Example 3:**

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

```

**Constraints:**

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are **unique**.

# Solutions

### Python

### 1. BFS

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque()
        
        q.append(0)
        
        word_set = set(wordDict)
        visited = set() # We don't have to re-consider same staring index
        
        while q:
            idx = q.popleft()
            if idx == len(s):
                return True
            
            if idx in visited:
                continue
                
            for end in range(idx + 1, len(s) + 1):
                if s[idx:end] in word_set:
                    q.append(end)
                    
            visited.add(idx)
                    
        return False
```

> Runtime: 77 ms, faster than 31.20% of Python3 online submissions for Word Break.
Memory Usage: 13.9 MB, less than 70.31% of Python3 online submissions for Word Break.
> 

### Complexity Analysis

- Time complexity : O(n*m*n), where n is the length of string and m is the number of words in dictionary. For every starting index, I did string comparison till the end of the given string. On top of that, I can have m words in the queue in the worst case.
- Space complexity : O(m) where m is the number of words in wordDict

### 2. DP

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        opt = [False] * (len(s) + 1)
        opt[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    opt[i] = opt[i + len(w)]
                if opt[i]:
                    break
        
        return opt[0]
```

Runtime: 73 ms, faster than 37.92% of Python3 online submissions for Word Break.
Memory Usage: 14.1 MB, less than 43.35% of Python3 online submissions for Word Break.

- Time complexity : O(n*m*n), where n is the length of string and m is the number of words in dictionary. For every starting index, I did string comparison till the end of the given string. On top of that, I can have m words in the queue in the worst case.
- Space complexity : O(m) where m is the number of words in wordDict

# Base Idea (One line)

1. Find all possible words at every index in the given string.

# Explanation

[Reference]

[Word Break - LeetCode](https://leetcode.com/problems/word-break/solution/)

[https://www.youtube.com/watch?v=Sx9NNgInc3A](https://www.youtube.com/watch?v=Sx9NNgInc3A)