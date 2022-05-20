# 101. Symmetric Tree

Acceptance: 51.7%
Difficulty: Easy
Frequency: 60.84%
Skills: BFS, BinaryTree, DFS, Tree
Solved: May 18, 2022

# Description

Given the `root` of a binary tree, *check whether it is a mirror of itself* (i.e., symmetric around its center).

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)

```
Input: root = [1,2,2,3,4,4,3]
Output: true

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)

```
Input: root = [1,2,2,null,3,null,3]
Output: false

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 1000]`.
- `100 <= Node.val <= 100`

**Follow up:**

Could you solve it both recursively and iteratively?

# Solutions

### Python

at first, level order traversal, then check each array is symmetric

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = []
        levels = []
        if root:
            q.append(root)
        while q:
            size = len(q)
            level = []
            for i in range(size):
                cur = q.pop(0)
                if cur == None:
                    level.append(None)
                    continue
                else:
                    level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                else:
                    q.append(None)
                if cur.right:
                    q.append(cur.right)
                else:
                    q.append(None)
            
            levels.append(level)
        
        for level in levels:
            n = len(level)
            if n == 1:
                continue
            mid = n//2
            print(level[:mid])
            print(level[:mid-1:-1])
            if level[:mid] != level[:mid-1:-1]:
                return False
        return True
```

> Runtime: 71 ms, faster than 8.64% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14.2 MB, less than 22.20% of Python3 online submissions for Symmetric Tree.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

### Python

Recursive way

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(t1,t2):
            if t1 == None and t2 == None:
                return True
            if t1 == None or t2 == None:
                return False
            
            if t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left):
                return True
            
        
        return isMirror(root,root)
```

> Runtime: 37 ms, faster than 79.77% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14 MB, less than 22.29% of Python3 online submissions for Symmetric Tree.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

### Python

Iterative way

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = []
        q.append(root)
        q.append(root)
        while q:
            t1 = q.pop(0)
            t2 = q.pop(0)
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val: return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True
```

> Runtime: 43 ms, faster than 60.36% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14 MB, less than 60.75% of Python3 online submissions for Symmetric Tree.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

# Base Idea (One line)

1. split into subproblems and implement recursively(or iteratively)
2. utilize level order traversal

# Explanation

[Reference]

[Symmetric Tree - LeetCode](https://leetcode.com/problems/symmetric-tree/solution/)