# 104. Maximum Depth of Binary Tree

Acceptance: 72.0%
Difficulty: Easy
Frequency: 47.64%
Skills: BFS, BinaryTree, DFS, Tree
Solved: May 19, 2022

# Description

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: 3

```

**Example 2:**

```
Input: root = [1,null,2]
Output: 2

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 104]`.
- `100 <= Node.val <= 100`

# Solutions

### Python

BFS until it reaches very bottom of tree and count the depth

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        
        q = []
        if root:
            q.append(root)
        while q:
            size = len(q)
            
            for i in range(size):
                cur = q.pop(0)
                    
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
            max_depth += 1
        return max_depth
```

> Runtime: 58 ms, faster than 46.75% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.2 MB, less than 90.31% of Python3 online submissions for Maximum Depth of Binary Tree.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

It requires to visit all nodes, so it takes O(n).

We use additional memory for queue and it can be at most O(n).

There would be many kinds of solutions such as using recursion. Refer to below solutions.

# Base Idea (One line)

1. BFS / DFS

# Explanation

[Reference]

[Maximum Depth of Binary Tree - LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/solution/)