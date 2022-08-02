# 739. Daily Temperatures

Acceptance: 67.6%
Difficulty: Medium
Frequency: 66.45%
Skills: Array, Monotonic Stack, Stack
Solved: August 1, 2022

# Description

Given an array of integers `temperatures` represents the daily temperatures, return *an array* `answer` *such that* `answer[i]` *is the number of days you have to wait after the* `ith` *day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Example 1:**

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

```

**Example 2:**

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

```

**Example 3:**

```
Input: temperatures = [30,60,90]
Output: [1,1,0]

```

**Constraints:**

- `1 <= temperatures.length <= 105`
- `30 <= temperatures[i] <= 100`

# Solutions

### Python

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0],0)]
        n = len(temperatures)
        answer = [0 * _ for _ in range(n)]
        for i in range(1,n):
            curr = temperatures[i]
            while stack and stack[-1][0] < curr:    
                answer[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((curr,i))
        return answer
```

> Runtime: 2032 ms, faster than 31.35% of Python3 online submissions for Daily Temperatures.
Memory Usage: 24.1 MB, less than 97.16% of Python3 online submissions for Daily Temperatures.
> 

### Complexity Analysis:

Given *N* as the length of `temperatures`,

- Time complexity: *O*(*N*)
    
    At first glance, it may look like the time complexity of this algorithm should be *O*(*N^*2), because there is a nested while loop inside the for loop. However, each element can only be added to the stack once, which means the stack is limited to N pops. Every iteration of the while loop uses 1 pop, which means the while loop will not iterate more than N*N* times in total, across all iterations of the for loop.
    
    An easier way to think about this is that in the worst case, every element will be pushed and popped once. This gives a time complexity of *O*(2⋅*N*)=*O*(*N*).
    
- Space complexity: *O*(*N*)
    
    If the input was non-increasing, then no element would ever be popped from the stack, and the stack would grow to a size of `N` elements at the end.
    
    Note: `answer` does not count towards the space complexity because space used for the output format does not count.
    

# Base Idea (One line)

1. Monotonic Stack

# Explanation

[Reference]

[Daily Temperatures - LeetCode](https://leetcode.com/problems/daily-temperatures/solution/)

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        hottest = 0
        answer = [0] * n
        
        for curr_day in range(n - 1, -1, -1):
            current_temp = temperatures[curr_day]
            if current_temp >= hottest:
                hottest = current_temp
                continue
            
            days = 1
            while temperatures[curr_day + days] <= current_temp:
                # Use information from answer to search for the next warmer day
                days += answer[curr_day + days]
            answer[curr_day] = days

        return answer
```