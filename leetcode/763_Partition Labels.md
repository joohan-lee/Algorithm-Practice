# 763. Partition Labels

Acceptance: 79.6%
Difficulty: Medium
Frequency: 49.14%
Skills: Greedy, Hash Table, String, Two Pointers
Solved: May 12, 2022

# Description

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return *a list of integers representing the size of these parts*.

**Example 1:**

```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

```

**Example 2:**

```
Input: s = "eccbbbbdec"
Output: [10]

```

**Constraints:**

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

# Solutions

### Python

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {c: i for i, c in enumerate(s)}
        end = anchor = 0

        ret = []
        for i, c in enumerate(s):
            # update the last index of current part
            end = max(end, last_idx[c])
            if i == end:
                ret.append(i - anchor +1)
                anchor = i+1

        return ret
```

> Runtime: 50 ms, faster than 65.49% of Python3 online submissions for Partition Labels.
> Memory Usage: 13.9 MB, less than 21.17% of Python3 online submissions for Partition Labels.

### Complexity Analysis

- Time complexity : O(n), where n is the length of string
- Space complexity : ~~O(n) to store last indices of each character~~
- **Space complexity:** <Caution!> Here the alphabet is at most 26, so we can actually say that space complexity is **O(1)**.

# Base Idea (One line)

1. Two pointers를 활용하기 위해 각 character의 last index를 hash에 저장.

# Explanation

[Reference]

[Partition Labels - LeetCode](https://leetcode.com/problems/partition-labels/solution/)
