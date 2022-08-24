# 42. Trapping Rain Water

Acceptance: 57.7%
Difficulty: Medium
Frequency: 98.00%
Skills: Array, Dynamic Programming, Monotonic Stack, Stack, Two Pointers
Solved: August 22, 2022
다시풀기: Required

# Description

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**

![https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

```

**Example 2:**

```
Input: height = [4,2,0,3,2,5]
Output: 9

```

**Constraints:**

- `n == height.length`
- `1 <= n <= 2 * 104`
- `0 <= height[i] <= 105`

# Solutions

### Python

### 1. Brute Force

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        for i in range(n):
            left_max = 0
            right_max = 0
            for j in range(i,-1,-1):
                left_max = max(left_max, height[j])
            for k in range(i,n):
                right_max = max(right_max, height[k])
            
            ans += min(left_max,right_max) - height[i]
        
        return ans
```

> Runtime: 
Memory Usage:
> 

Time Limit Exceeded

### Complexity Analysis

- Time complexity : O(n^2)
- Space complexity : O(1)

### 2. Dynamic Programming

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # get left_max at each index i
        left_max = [height[0]]
        for i in range(1, n):
            left_max.append(max(height[i],left_max[i-1]))
        
        # get right_max at each index i
        right_max = [0] * n
        right_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            right_max[i] = max(height[i], right_max[i+1])
        
        # iterate over the height array and update ans
        ans = 0
        for i in range(n):
            ans += min(left_max[i],right_max[i]) - height[i]
        
        return ans
```

> Runtime: 231 ms, faster than 33.28% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 16 MB, less than 81.74% of Python3 online submissions for Trapping Rain Water.
> 

### Complexity Analysis

- Time complexity : O(N), where N is the length of height array. Technically, O(3N)
- Space complexity : O(N)

### 3. Using Stacks

```python

```

> Runtime:
Memory Usage:
> 

### Complexity Analysis

- Time complexity :
- Space complexity :

# Base Idea (One line)

1. The volume of water at index i is ‘min(left_max[i], right_max[i]) - height[i]’.

# Explanation

[Reference]

[Trapping Rain Water - LeetCode](https://leetcode.com/problems/trapping-rain-water/solution/)