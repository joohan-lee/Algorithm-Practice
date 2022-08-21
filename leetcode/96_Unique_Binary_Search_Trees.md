# 96. Unique Binary Search Trees

Acceptance: 59.0%
Difficulty: Medium
Frequency: 55.97%
Skills: Binary Search Tree, BinaryTree, Dynamic Programming, Math, Tree
Solved: August 20, 2022
다시풀기: Required

# Description

Given an integer `n`, return *the number of structurally unique **BST'**s (binary search trees) which has exactly* `n` *nodes of unique values from* `1` *to* `n`.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg](https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg)

```
Input: n = 3
Output: 5

```

**Example 2:**

```
Input: n = 1
Output: 1

```

**Constraints:**

- `1 <= n <= 19`

# Solutions

### Python

```python
class Solution:
    def numTrees(self, n: int) -> int:
        # 모든 경우를 구하는 것이 아니고, 경우의 수를 구하므로 Bottom-up DP 가능성
        
        G = [0] * (n+1)
        G[0], G[1] = 1, 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j - 1] * G[i - j]
                
        return G[n]
```

> Runtime: 50 ms, faster than 43.15% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 13.9 MB, less than 12.74% of Python3 online submissions for Unique Binary Search Trees.
> 

### Complexity Analysis

- Time complexity : the main computation of the algorithm is done at the statement with `G[i]`. So the time complexity is essentially the number of iterations for the statement, which is ∑(*i*=2,*n)**i*=(2+*n*)(*n*−1)/2, to be exact, therefore the time complexity is *O*(*N^*2)
- Space complexity : The space complexity of the above algorithm is mainly the storage to keep all the intermediate solutions, therefore *O*(*N*).

# Base Idea (One line)

1. 2-dimensional DP → 1-dimensional DP. Only the number of BST matters.([1,2,3] and [4,5,6] has same number of unique BST.)

# Explanation

[Reference]

[Unique Binary Search Trees - LeetCode](https://leetcode.com/problems/unique-binary-search-trees/solution/)