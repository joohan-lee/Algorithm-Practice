# 102. Binary Tree Level Order Traversal

Acceptance: 61.0%
Difficulty: Medium
Frequency: 57.43%
Skills: BFS, BinaryTree, Tree
Solved: May 18, 2022

# Description

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

```

**Example 2:**

```
Input: root = [1]
Output: [[1]]

```

**Example 3:**

```
Input: root = []
Output: []

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
- `1000 <= Node.val <= 1000`

# Solutions

### Python

Iterative

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = []
        if root:
            queue.append(root)
        while queue:
            size = len(queue)
            cur_level=[]
            for i in range(size):
                cur = queue.pop(0)
                cur_level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            res.append(cur_level)
        return res
```

> Runtime: **37 ms(82.43%)**
Memory Usage: **14.2 MB(52.73%)**
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

### Python

Recursive

```python
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        level = 0
        if root == None:
            return []
        
        def bfs(cur, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(cur.val)
                
            if cur.left:
                bfs(cur.left, level + 1)
            if cur.right:
                bfs(cur.right, level + 1)
        
        bfs(root,level)
        
        return levels
```

> Runtime: 79 ms, faster than 5.10% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 15 MB, less than 9.24% of Python3 online submissions for Binary Tree Level Order Traversal.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

# Base Idea (One line)

1. BFS using queue
2. BFS recursively without queue

# Explanation

[Reference]

[Binary Tree Level Order Traversal - LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/solution/)