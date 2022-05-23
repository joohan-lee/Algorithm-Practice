# 250. Count Univalue Subtrees

Acceptance: 54.8%
Difficulty: Medium
Frequency: 31.22%
Skills: BinaryTree, DFS, Tree
Solved: May 20, 2022
다시풀기: Required

# Description

Given the `root` of a binary tree, return the number of **uni-value** subtrees.

A **uni-value subtree** means all nodes of the subtree have the same value.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/08/21/unival_e1.jpg](https://assets.leetcode.com/uploads/2020/08/21/unival_e1.jpg)

```
Input: root = [5,1,5,5,5,null,5]
Output: 4

```

**Example 2:**

```
Input: root = []
Output: 0

```

**Example 3:**

```
Input: root = [5,5,5,5,5,null,5]
Output: 6

```

**Constraints:**

- The number of the node in the tree will be in the range `[0, 1000]`.
- `1000 <= Node.val <= 1000`

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
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root)
        return self.count
    
    
    def dfs(self, root):
    # it is implemented implement bottom-up.     
    
        if not root:
            return True
        
        # If a leaf node
        if not root.left and not root.right:
            self.count += 1
            return True
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        #### root에 대한 처리
        # If left and right subrees are univalue AND their values are equal to root
        if left and right and root.left and root.right and root.left.val == root.val and root.right.val == root.val:
            self.count += 1
            return True
        
        # If there is no right subtree AND left subtree is univalue AND left subtree value is equal to root
        if not root.right and left and root.left and root.left.val == root.val:
            self.count += 1
            return True
        
        # If there is no left subtree AND right subtree is univalue AND right subtree value is equal to root
        if not root.left and right and root.right and root.right.val == root.val:
            self.count += 1
            return True
        
        # In any other case, return False    
        return False
```

> Runtime: 
Memory Usage:
> 

### Complexity Analysis

- Time complexity :
- Space complexity :

# Base Idea (One line)

1. bottom-up traversal

# Explanation

[Reference]

[Account Login - LeetCode](https://leetcode.com/problems/count-univalue-subtrees/discuss/1857124/Python-DFS)