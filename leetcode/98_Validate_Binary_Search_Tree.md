# 98. Validate Binary Search Tree

Acceptance: 31.6%
Difficulty: Medium
Frequency: 64.88%
Skills: BFS, BinaryTree, DFS, Tree
Solved: September 16, 2022

# Description

Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.

A **valid BST** is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

```
Input: root = [2,1,3]
Output: true

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 104]`.
- `231 <= Node.val <= 231 - 1`

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, lower, upper):
            if not root:
                return True
            
            left = validate(root.left, lower, root.val)
            right = validate(root.right, root.val, upper)
            
            
            if root.val <= lower or root.val >= upper:
                return False
            
            return left and right
        
        return validate(root, -math.inf, math.inf)
```

> Runtime: 62 ms, faster than 68.79% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 17 MB, less than 15.01% of Python3 online submissions for Validate Binary Search Tree.
> 

### Complexity Analysis

- Time complexity : O(n) where n is the number of nodes
- Space complexity : O(n)

# Base Idea (One line)

1. DFS with lower and upper bounds

# Explanation

[Reference]

[Validate Binary Search Tree - LeetCode](https://leetcode.com/problems/validate-binary-search-tree/solution/)