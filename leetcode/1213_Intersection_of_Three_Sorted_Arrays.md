# 1213. Intersection of Three Sorted Arrays

Acceptance: 80.0%
Difficulty: Easy
Frequency: 24.74%
Skills: Array, Binary Search, Counting, Hash Table, Two Pointers
Solved: June 13, 2022

# Description

Given three integer arrays `arr1`, `arr2` and `arr3` **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.

**Example 1:**

```
Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation:Only 1 and 5 appeared in the three arrays.

```

**Example 2:**

```
Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
Output: []

```

**Constraints:**

- `1 <= arr1.length, arr2.length, arr3.length <= 1000`
- `1 <= arr1[i], arr2[i], arr3[i] <= 2000`

# Solutions

### Python

Hash Map

```python
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        h = {}
        for num in arr1:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
        for num in arr2:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
        for num in arr3:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
                
        ret = []
        for key, value in h.items():
            if value == 3:
                ret.append(key)
        ret.sort()
        
        return ret
```

> Runtime: 94 ms, faster than 80.69% of Python3 online submissions for Intersection of Three Sorted Arrays.
Memory Usage: 14.3 MB, less than 15.56% of Python3 online submissions for Intersection of Three Sorted Arrays.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

### Python

Three pointers

```python
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        p1 = p2 = p3 = 0
        ans = []
        
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                ans.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            
            else:
                # p1과 p2 먼저 비교하다가 같은 element있으면
                if arr1[p1] < arr2[p2]:
                    p1 += 1
                # p2와 p3 도 포인터 맞춰 줌.
                elif arr2[p2] < arr3[p3]:
                    p2 += 1
                else:
                    p3 += 1
        return ans
```

> Runtime: 165 ms, faster than 22.82% of Python3 online submissions for Intersection of Three Sorted Arrays.
Memory Usage: 14.3 MB, less than 44.29% of Python3 online submissions for Intersection of Three Sorted Arrays.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(1)

# Base Idea (One line)

1. Count the common elements using hash table

# Explanation

[Reference]

[Account Login - LeetCode](https://leetcode.com/problems/intersection-of-three-sorted-arrays/solution/)