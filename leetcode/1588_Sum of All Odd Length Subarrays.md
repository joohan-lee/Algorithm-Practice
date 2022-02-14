# 1588. Sum of All Odd Length Subarrays

Acceptance: 0.828
Difficulty: Easy
Skills: array, subarray
Solved: January 25, 2022

# Description

Given an array of positive integers `arr`, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return *the sum of all odd-length subarrays of* `arr`.

# Examples

**Example 1:**

```
Input: arr = [1,4,2,5,3]
Output: 58
Explanation:The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
```

**Example 2:**

```
Input: arr = [1,2]
Output: 3
Explanation:There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
```

**Example 3:**

```
Input: arr = [10,11,12]
Output: 66

```

# **Constraints:**

- `1 <= arr.length <= 100`
- `1 <= arr[i] <= 1000`

# Solutions

### Python

```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        len_arr = len(arr)
        sumAll = 0
        for i in range(1,len_arr+1,2):
            for j in range(len_arr):
                if j + i <= len_arr: #등호에 주의
                    sumAll += sum(arr[j:j+i])
                else:
                    pass
        return sumAll
```

> Runtime: 76 ms, faster than 42.77% of Python3 online submissions for Sum of All Odd Length Subarrays.
Memory Usage: 14.3 MB, less than 50.60% of Python3 online submissions for Sum of All Odd Length Subarrays.
> 

# 해설