# 53. Maximum Subarray

- Acceptance: 49.4%
- Frequency : 94.08%
- Difficulty: Easy
- Skills: Array, Dynamic Programming, Divide and Conquer
- Solved: February 22, 2022

# Description

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return *its sum*.

A **subarray** is a **contiguous** part of an array.

**Example 1:**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

```

**Example 2:**

```
Input: nums = [1]
Output: 1

```

**Example 3:**

```
Input: nums = [5,4,-1,7,8]
Output: 23

```

**Constraints:**

- `1 <= nums.length <= 105`
- `104 <= nums[i] <= 104`

**Follow up**: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Solutions

### Python

### 1. Optimized Brute Force

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            cur_subarray = 0
            for j in range(i,len(nums)):
                cur_subarray += nums[j]
                max_subarray = max(max_subarray, cur_subarray)
        return max_subarray
```

> O(N^2) time. This exceeds time limit.

```python
# Just make subarray
arr = [3, 5, 1, 2, 4]
sub = []
for i in range(len(arr)):
    for j in range(len(arr)):
        if j+i+1 <= len(arr):
            sub.append(arr[j:j+i+1])

print(sub)
```

### 2. Dynamic Programming, Kadane's Algorithm

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            # if current_subarray is negative, throw it away. Otherwise, keep adding to it.
            cur = max(nums[i], cur+nums[i])
            max_sum = max(max_sum, cur)

        return max_sum
```

[Kadane's Algorithm](https://www.interviewbit.com/blog/maximum-subarray-sum/#:~:text=Kadane's%20Algorithm%20is%20an%20iterative,ending%20at%20the%20previous%20position.&text=Define%20two%2Dvariable%20currSum%20which,stores%20maximum%20sum%20so%20far).

- O(N) time, where N is the length of nums.
- O(1) space complexity, we are using only 2 variables(cur, max_sum)

> Runtime: 891 ms, faster than 58.99% of Python3 online submissions for Maximum Subarray.
> Memory Usage: 28 MB, less than 73.35% of Python3 online submissions for Maximum Subarray.

### 3. Divide & Conquer

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            #take an input left and right, which defines the bounds of the array.

            #Base case - empty array
            if left > right:
                return -math.inf

            mid = (left+right) >> 1
            cur = best_left_sum = best_right_sum = 0

            #iterate from the middle to the beginning.
            for i in range(mid-1, left-1, -1):
                cur += nums[i]
                best_left_sum = max(cur, best_left_sum)

            cur = 0
            for i in range(mid+1, right+1):
                cur += nums[i]
                best_right_sum = max(cur,best_right_sum)

            # the best_combined_sum uses the middle element and the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            #Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid-1)
            right_half = findBestSubarray(nums, mid+1, right)

            #The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)

        return findBestSubarray(nums,0,len(nums)-1)
```

### Complexity Analysis

- Time complexity : O(N logN), where N is the length of nums.
  <br>On our first call to findBestSubarray, we use for loops to visit every element of nums. Then, we split the array in half and call findBestSubarray with each half. Both those calls will then iterate through every element in that half, which combined is every element of nums again. Then, both those halves will be split in half, and 4 more calls to findBestSubarray will happen, each with a quarter of nums. As you can see, every time the array is split, we still need to handle every element of the original input nums. We have to do this \log NlogN times since that's how many times an array can be split in half.

- Space complexity : O(logN), where N is the length of nums.<br>The extra space we use relative to input size is solely occupied by the recursion stack. Each time the array gets split in half, another call of findBestSubarray will be added to the recursion stack, until calls start to get resolved by the base case - remember, the base case happens at an empty array, which occurs after \log NlogN calls.

# Base Idea (One line)

1. Brute Force O(N^2) time
2. DP, O(N) time, O(1) space
3. Recursion, O(n logn) time, O(logn) space

# Explanation

[Reference]

[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/solution/)
