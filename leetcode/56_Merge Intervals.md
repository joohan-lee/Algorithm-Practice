# 56. Merge Intervals

Acceptance: 0.44799999999999995
Difficulty: Medium
Frequency: 0.9898
Skills: Array, Sorting
Solved: January 29, 2022

# Description

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

**Example 1:**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

```

**Example 2:**

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

```

**Constraints:**

- `1 <= intervals.length <= 104`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 104`

# Solutions

### Python

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x:x[0]) #sort by start time
        ret = [sorted_intervals[0]]
        j = 0
        for i in range(1, len(sorted_intervals)):
            interval = sorted_intervals[i]
            if ret[j][1] >= interval[0]:
                #merge
                ret[j][1] = max(ret[j][1], interval[1])
            else:
                ret.append(interval)
                j += 1
        return ret
```

> Runtime: 219 ms, faster than 39.35% of Python3 online submissions for Merge Intervals.
Memory Usage: 18.1 MB, less than 53.37% of Python3 online submissions for Merge Intervals.
> 

### Complexity Analysis

- Time complexity : O(nlogn), to sort the array
- Space complexity : O(n), in the worst case, there would be no overlapping. Then, we have to store whole array to ret.

# Base Idea (One line)

1. sort the array by start time and when merging, choose latest end time.

# Explanation

[Reference]

[Merge Intervals - LeetCode](https://leetcode.com/problems/merge-intervals/solution/)

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
```