# 78. Subsets

Acceptance: 72.7%
Difficulty: Medium
Frequency: 73.83%
Skills: Array, Backtracking, bit manipulation
Solved: July 28, 2022
다시풀기: Required

# Description

Given an integer array `nums` of **unique** elements, return *all possible subsets (the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

```

**Example 2:**

```
Input: nums = [0]
Output: [[],[0]]

```

**Constraints:**

- `1 <= nums.length <= 10`
- `10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

# Solutions

### Python

### 1. Cascading

```python
from collections import deque
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res
```

> Runtime: 31 ms, faster than 97.44% of Python3 online submissions for Subsets.
Memory Usage: 14 MB, less than 96.28% of Python3 online submissions for Subsets.
> 

### Complexity Analysis

- Time complexity: O(*N*×2^*N*) to generate all subsets and then copy them into output list.
- Space complexity: O(*N*×2^*N*). This is exactly the number of solutions for subsets multiplied by the number N*N* of elements to keep for each subset.
    - For a given number, it could be present or absent (*i.e.* binary choice) in a subset solution. As as result, for *N* numbers, we would have in total 2^*N* choices (solutions).

### 2. Backtracking

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
            
            
        res = []
        n = len(nums)
        for k in range(n+1):
            backtrack()
        return res
```

> Runtime: 47 ms, faster than 64.77% of Python3 online submissions for Subsets.
Memory Usage: 14.2 MB, less than 33.99% of Python3 online submissions for Subsets.
> 

### Complexity Analysis

- Time complexity: O(*N*×2^*N*) to generate all subsets and then copy them into output list.
- Space complexity: O(*N*). We are using *O*(*N*) space to maintain `curr`, and are modifying `curr` in-place with backtracking. Note that for space complexity analysis, we do not count space that is *only* used for the purpose of returning output, so the `output` array is ignored.

# Base Idea (One line)

1. Recursion, Backtracking

# Explanation

[Reference]

[Subsets - LeetCode](https://leetcode.com/problems/subsets/solution/)

[https://www.youtube.com/watch?v=-eVkq8odxno](https://www.youtube.com/watch?v=-eVkq8odxno) [해설 참고영상]