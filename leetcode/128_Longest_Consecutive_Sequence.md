# 128. Longest Consecutive Sequence

Acceptance: 49.0%
Difficulty: Medium
Frequency: 83.97%
Skills: Array, Hash Table, Union Find
Solved: September 20, 2022

# Description

Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in `O(n)` time.

**Example 1:**

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is[1, 2, 3, 4]. Therefore its length is 4.

```

**Example 2:**

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

```

**Constraints:**

- `0 <= nums.length <= 105`
- `109 <= nums[i] <= 109`

# Solutions

### Python

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in hash_map:
                hash_map[num] = False
        
        longest = 0
        for k, v in hash_map.items():
            temp = 1
            up = k+1
            while up in hash_map and not hash_map[up]:
                hash_map[up] = True
                up += 1
                temp += 1
            down = k-1
            while down in hash_map and not hash_map[down]:
                hash_map[down] = True
                down -= 1
                temp += 1
            
            longest = max(longest, temp)
                
        
        return longest
```

> Runtime: 523 ms, faster than 72.57% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 32.4 MB, less than 12.80% of Python3 online submissions for Longest Consecutive Sequence.
> 

### Complexity Analysis

- Time complexity : O(N)
- Space complexity : O(N)

# Base Idea (One line)

1. Use hash table to figure out if consecutive number exists.

# Explanation

[Reference]

[Longest Consecutive Sequence - LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/solution/)

```python
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
```