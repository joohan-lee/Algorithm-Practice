# 14. Longest Common Prefix

Acceptance: 39.7%
Difficulty: Easy
Frequency: 90.49%
Skills: String
Solved: June 7, 2022

# Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

```
Input: strs = ["flower","flow","flight"]
Output: "fl"

```

**Example 2:**

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

```

**Constraints:**

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lower-case English letters.

# Solutions

### Python

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        n = len(strs)
            
        common_prefix = strs[0]
        
        for i in range(n):
            curr_str = strs[i]
            j = 0
            while j < len(common_prefix) and j < len(curr_str) and common_prefix[j] == curr_str[j]:
                j += 1
            if j == 0:
                return ""
            common_prefix = common_prefix[:j]
        return common_prefix
```

> Runtime: 35 ms, faster than 88.91% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14 MB, less than 48.86% of Python3 online submissions for Longest Common Prefix.
> 

### Complexity Analysis

- Time complexity : O(S), where S is the sum of all characters in all strings.
- Space complexity : O(1). Only used constant extra space.

# Base Idea (One line)

1. Greedy approach. (Always find the maximum length of common prefix)

# Explanation

[Reference]

For this problem, we can solve in other ways such as D&C, Binary Search. Refer to below.

[Longest Common Prefix - LeetCode](https://leetcode.com/problems/longest-common-prefix/solution/)

From other user, [grl_pwr](https://leetcode.com/grl_pwr), I could see a good solution which uses Python’s strength.

```python
def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=[]
        num = len(strs)
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix) ```
```