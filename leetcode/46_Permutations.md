# 46. Permutations

Acceptance: 72.8%
Difficulty: Medium
Frequency: 70.60%
Skills: Array, Backtracking
Solved: June 8, 2022
다시풀기: Required

# Description

Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```

**Example 2:**

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]

```

**Example 3:**

```
Input: nums = [1]
Output: [[1]]

```

**Constraints:**

- `1 <= nums.length <= 6`
- `10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

# Solutions

### Python

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first = 0):
            if first == n:
                output.append(nums[:])

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]


        n = len(nums)
        output = []
        backtrack()
        return output
```

> Runtime: 82 ms, faster than 8.78% of Python3 online submissions for Permutations.
> Memory Usage: 14.1 MB, less than 21.70% of Python3 online submissions for Permutations.

### Complexity Analysis

![46](source/46.png.png)

# Base Idea (One line)

1. Backtracking. Swap each element repeatedly.

# Explanation

[Reference]

[Permutations - LeetCode](https://leetcode.com/problems/permutations/solution/)

<파이썬에서 파라미터로 받은 배열>

output.append(nums)

output.append(nums[:])

위 두 코드가 같은 결과를 초래할 것 같았는데, 달랐다.

메모리 주소를 찍어보니 nums는 초기 받은 파라미터 배열의 주소를 가리키고, nums[:]는 계속 값이 변했다. 아무래도, 파라미터로 받은 배열을 조작하면 배열이 copy되어 조작되는듯 하다.

```python
from collections import deque
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        print(id(nums), "!!")

        def backtrack(first = 0):
            if first == n:
                print(id(nums))
                print(id(nums[:]))
                # output.append(nums[:])
                output.append(nums) # 항상 [1,2,3]
                print('2', nums) # 받은 값 출력
                # 즉, print 할때는 nums가 변화하는 값들을 가리키고,
                # append할때는 nums가 처음 파라미터로 받은 배열의 주소에 들은 배열 값들을 가리킨다..
                # return

            for i in range(first, n):
                print(id(nums[first]))
                nums[first], nums[i] = nums[i], nums[first]
                print('1',nums)
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]


        n = len(nums)
        output = []
        backtrack()
        return output
```
