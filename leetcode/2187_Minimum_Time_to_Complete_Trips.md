# 2187. Minimum Time to Complete Trips

Acceptance: 32.1%
Difficulty: Medium
Frequency: 57.32%
Skills: Array, Binary Search
Solved: December 30, 2022

# Description

You are given an array `time` where `time[i]` denotes the time taken by the `ith` bus to complete **one trip**.

Each bus can make multiple trips **successively**; that is, the next trip can start **immediately after** completing the current trip. Also, each bus operates **independently**; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer `totalTrips`, which denotes the number of trips all buses should make **in total**. Return *the **minimum time** required for all buses to complete **at least*** `totalTrips` *trips*.

**Example 1:**

```
Input: time = [1,2,3], totalTrips = 5
Output: 3
Explanation:
- At time t = 1, the number of trips completed by each bus are [1,0,0].
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0].
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1].
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.

```

**Example 2:**

```
Input: time = [2], totalTrips = 1
Output: 2
Explanation:
There is only one bus, and it will complete its first trip at t = 2.
So the minimum time needed to complete 1 trip is 2.

```

**Constraints:**

- `1 <= time.length <= 105`
- `1 <= time[i], totalTrips <= 107`

# Solutions

### Python

```python
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        maxTime = time[0] * totalTrips

        minTime = maxTime
        left = 1
        right = maxTime
        while left <= right:
            mid = left + (right - left) // 2
            currTrip = 0
            for i in range(len(time)):
                currTrip += mid // time[i]

            if currTrip == totalTrips:
                # if required number of trips is equal to totalTrips, it should be minimum time.
                minTime = min(minTime, mid)
                right = mid - 1
            elif currTrip < totalTrips:
                left = mid + 1
            elif currTrip > totalTrips:
                minTime = min(minTime, mid)
                right = mid - 1

        return minTime
```

> Runtime: 
Memory Usage:
> 

### Complexity Analysis

- Time complexity : O(nlogn). For sorting, it takes O(nlogn). Iterating through all elements while binary search(O(logn) takes O(nlogn).
- Space complexity : O(1)

# Base Idea (One line)

1. Find the maximum number of trips, and then find the possible minimum number of trips between 1 to the maximum.

# Explanation

[Reference]