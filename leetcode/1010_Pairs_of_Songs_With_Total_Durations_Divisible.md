# 1010. Pairs of Songs With Total Durations Divisible by 60

Acceptance: 53.0%
Difficulty: Medium
Frequency: 91.69%
Skills: Array, Counting, Hash Table
Solved: November 10, 2022
다시풀기: Required

# Description

You are given a list of songs where the `ith` song has a duration of `time[i]` seconds.

Return *the number of pairs of songs for which their total duration in seconds is divisible by* `60`. Formally, we want the number of indices `i`, `j` such that `i < j` with `(time[i] + time[j]) % 60 == 0`.

**Example 1:**

```
Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

```

**Example 2:**

```
Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

```

**Constraints:**

- `1 <= time.length <= 6 * 104`
- `1 <= time[i] <= 500`

# Solutions

### Python

```python
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # initialize dict to all zeros.
        remainder_map = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0:
                ret += remainder_map[0] # Since nCn-1 = n , we can just add n.
            else:
                ret += remainder_map[60 -(t % 60)]
            remainder_map[t%60] += 1
        
        return ret
```

### Complexity Analysis

- Time complexity :
- Space complexity :

# Base Idea (One line)

1. Reducible to Two Sum. If there is complement in hash map, we can directly add the number of complements.

# Explanation

[Reference]

[](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/solutions/934744/pairs-of-songs-with-total-durations-divisible-by-60/)