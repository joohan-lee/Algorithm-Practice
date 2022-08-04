# 1046. Last Stone Weight

Acceptance: 64.6%
Difficulty: Medium
Frequency: 52.59%
Skills: Array, Heap
Solved: August 4, 2022

# Description

You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

- If `x == y`, both stones are destroyed, and
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return *the weight of the last remaining stone*. If there are no stones left, return `0`.

**Example 1:**

```
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

```

**Example 2:**

```
Input: stones = [1]
Output: 1

```

**Constraints:**

- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

# Solutions

### Python

```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            r1 = heapq.heappop(heap) * (-1)
            r2 = heapq.heappop(heap) * (-1)
            if r1 > r2:
                heapq.heappush(heap, r2 - r1)
        return 0 if len(heap) == 0 else -heap[0]
```

> Runtime: 54 ms, faster than 38.12% of Python3 online submissions for Last Stone Weight.
Memory Usage: 13.9 MB, less than 62.45% of Python3 online submissions for Last Stone Weight.
> 

### Complexity Analysis

Let *N* be the **length of stones**.

- Time complexity : *O*(*N*log*N*).
    
    Converting an array into a Heap takes *O*(*N*) time (it isn't actually sorting; it's putting them into an order that allows us to get the maximums, each in *O*(log*N*) time).
    
    Like before, the main loop iterates up to *N*−1 times. This time however, it's doing up to three *O*(log*N*) operation each time; two removes, and an optional add. Like always, the three is an ignored constant. This means that we're doing *N*⋅*O*(log*N*)=*O*(*N*log*N*) operations.
    
- Space complexity : *O*(*N*) or *O*(log*N*).
    
    In Python, converting a list to a heap is done in-place, requiring *O*(1) auxillary space, giving a total space complexity of *O*(1). Modifying the input has its pros and cons; it saves space, but it means that other functions can't use the same array.
    
    In Java though, it's *O*(*N*) to create the `PriorityQueue`.
    
    We could reduce the space complexity to *O*(1) by implementing our own iterative heapfiy, if needed.
    

# Base Idea (One line)

1. Max Heap

# Explanation

[Reference]

[Last Stone Weight - LeetCode](https://leetcode.com/problems/last-stone-weight/solution/)