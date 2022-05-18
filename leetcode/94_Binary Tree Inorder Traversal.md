# 94. Binary Tree Inorder Traversal

Acceptance: 70.9%
Difficulty: Easy
Frequency: 50.14%
Skills: BinaryTree, DFS, Stack, Tree
Solved: May 17, 2022

# Description

Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```
Input: root = [1,null,2,3]
Output: [1,3,2]

```

**Example 2:**

```
Input: root = []
Output: []

```

**Example 3:**

```
Input: root = [1]
Output: [1]

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `100 <= Node.val <= 100`

# Solutions

### Python

<Recursive version>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive version
        q = []
        def inorderTraversal(root):
            if root != None:
                inorderTraversal(root.left)
                q.append(root.val)
                inorderTraversal(root.right)
        
        inorderTraversal(root)
        
        return q
```

> Runtime: 61 ms, faster than 9.32% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.8 MB, less than 60.47% of Python3 online submissions for Binary Tree Inorder Traversal.
> 

### Complexity Analysis

- Time complexity : O(n), where n is the number of nodes, because we visit all nodes
    
    T(n) = 2T(n/2) + 1
    
- Space complexity : O(n)

<Iterative version using stack>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative version
        stack = []
        res = []
        cur = root
        while cur != None or stack != []:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res
```

> Runtime: 38 ms, faster than 61.52% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.9 MB, less than 60.47% of Python3 online submissions for Binary Tree Inorder Traversal.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

# Base Idea (One line)

1. Recursively traverse the tree
2. Iteratively traverse the tree using a stack

# Explanation

[Reference]

[Binary Tree Inorder Traversal - LeetCode](https://leetcode.com/problems/binary-tree-inorder-traversal/solution/)