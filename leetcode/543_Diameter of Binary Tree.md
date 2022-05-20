# 543. Diameter of Binary Tree

Acceptance: 54.4%
Difficulty: Easy
Frequency: 70.85%
Skills: BinaryTree, DFS, Tree
Solved: May 19, 2022
다시풀기: Required

# Description

Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

```

**Example 2:**

```
Input: root = [1,2]
Output: 1

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 104]`.
- `100 <= Node.val <= 100`

# Solutions

### Python

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        
        def helper(cur):
            if cur == None:
                return 0
            
            nonlocal max_len
            
            left = helper(cur.left)
            right = helper(cur.right)
            
            max_len = max(max_len, left + right)
            
            return max(left, right) + 1
        helper(root)
        return max_len
```

> Runtime: 54 ms, faster than 66.88% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 16.4 MB, less than 42.93% of Python3 online submissions for Diameter of Binary Tree.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

# Base Idea (One line)

1. DFS

# Explanation

[Reference]

[Diameter of Binary Tree - LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/solution/)