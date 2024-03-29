# 1710. Maximum Units on a Truck

Acceptance: 72.0%
Difficulty: Easy
Frequency: 69.39%
Skills: Array, Greedy, Sorting
Solved: May 10, 2022

# Description

You are assigned to put some amount of boxes onto **one truck**. You are given a 2D array `boxTypes`, where `boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]`:

- `numberOfBoxesi` is the number of boxes of type `i`.
- `numberOfUnitsPerBoxi`is the number of units in each box of the type `i`.

You are also given an integer `truckSize`, which is the **maximum** number of **boxes** that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed `truckSize`.

Return *the **maximum** total number of **units** that can be put on the truck.*

**Example 1:**

```
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

```

**Example 2:**

```
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

```

**Constraints:**

- `1 <= boxTypes.length <= 1000`
- `1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000`
- `1 <= truckSize <= 106`

# Solutions

### Python

```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        sum = 0
        cur_box = 0
        for arr in boxTypes:
            if cur_box + arr[0] < truckSize:
                sum += arr[0] * arr[1]
                cur_box += arr[0]
            else:
                sum += (truckSize - cur_box) * arr[1]
                cur_box += (truckSize - cur_box)
        return sum
```

> Runtime: 176 ms, faster than 70.52% of Python3 online submissions for Maximum Units on a Truck.
Memory Usage: 14.4 MB, less than 32.49% of Python3 online submissions for Maximum Units on a Truck.
> 

### Complexity Analysis

- Time complexity : O(nlogn) , to sort boxTypes
- Space complexity : O(1)

# Base Idea (One line)

1. 리스트 두번째 값을 기준으로 정렬 후 greedy로 채워나가기.

# Explanation

[Reference]

[Maximum Units on a Truck - LeetCode](https://leetcode.com/problems/maximum-units-on-a-truck/solution/)