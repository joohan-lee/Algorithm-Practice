# 11. Container With Most Water

Acceptance: 54.0%
Difficulty: Medium
Frequency: 84.31%
Skills: Array, Greedy, Two Pointers
Solved: May 31, 2022

# Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

**Example 1:**

![https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

```

**Example 2:**

```
Input: height = [1,1]
Output: 1

```

**Constraints:**

- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 104`

# Solutions

### Python

Brute-Force. For this problem, brute force is pretty straight forward, but I will improve this.

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force
        max_val = 0
        for left in range(len(height)):
            for right in range(left+1, len(height)):
                width = right - left
                max_val = max(max_val, min(height[left],height[right])*width)
        return max_val
```

### Python

Greedy and Two Pointers. The intuition behind this approach is that the area formed between the lines will **always be limited by the height of the shorter line**. Further, the farther the lines, the more will be the area obtained.

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two Poninters, Greedy
        left = 0
        right = len(height) - 1
        
        maxArea = 0
        while left < right:
            width = right - left
            maxArea = max(maxArea, width * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea
```

> Runtime: 1254 ms, faster than 16.61% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.6 MB, less than 16.56% of Python3 online submissions for Container With Most Water.
> 

### Complexity Analysis

- Time complexity : O(n), single pass.
- Space complexity : O(1)

# Base Idea (One line)

1. Take two pointers, one at the beginning and one at the end of the array.

# Explanation

[Reference]

[Container With Most Water - LeetCode](https://leetcode.com/problems/container-with-most-water/solution/)