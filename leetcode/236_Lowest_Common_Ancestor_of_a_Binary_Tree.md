# 236. Lowest Common Ancestor of a Binary Tree

Acceptance: 57.4%
Difficulty: Medium
Frequency: 86.45%
Skills: BinaryTree, DFS, Recursion, Tree
Solved: August 26, 2022

# Description

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

**Example 1:**

![https://assets.leetcode.com/uploads/2018/12/14/binarytree.png](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2018/12/14/binarytree.png](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

```

**Example 3:**

```
Input: root = [1,2], p = 1, q = 2
Output: 1

```

**Constraints:**

- The number of nodes in the tree is in the range `[2, 105]`.
- `109 <= Node.val <= 109`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the tree.

# Solutions

### Python

### 1. Recursive Approach

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            nonlocal ans
            if not node:
                return False
            
            mid = (node == p) or (node == q)
            left = dfs(node.left)
            right = dfs(node.right)
            if mid + left + right >=2:
                ans = node
            
            return left or right or mid
        
        ans = None
        dfs(root)
        
        return ans
```

> Runtime: 87 ms, faster than 78.55% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 26.3 MB, less than 64.33% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
> 

### Complexity Analysis

- Time complexity : O(N), where N is the number of nodes. In the worst case, I should visit all nodes in the tree.
- Space complexity : O(N)

### 2. Iterative approach using parent pointers

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        anc_dict = {root:None}
        p_anc = []
        q_anc = []
        ans = None
        
        stack = [root]
        # build a dictionary that stores all parent pointers of nodes
        while stack:
            curr = stack.pop()
            if curr.left:
                anc_dict[curr.left] = curr
                stack.append(curr.left)
            if curr.right:
                anc_dict[curr.right] = curr
                stack.append(curr.right)
        
        
        # p ancestors
        while p:
            p_anc.append(p)
            p = anc_dict[p]
        
        while q:
            if q in p_anc:
                ans = q
                break
            q = anc_dict[q]
            
        return ans
```

> Runtime: 166 ms, faster than 10.77% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 18.1 MB, less than 98.62% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
> 
- Time complexity : O(N), where N is the number of nodes. In the worst case, I should visit all nodes in the tree.
- Space complexity : O(N)

# Base Idea (One line)

1. Once we hit the p or q, we return True for all its ancestors, using Recursion.
2. Build a dictionary that stores parent pointers of all nodes.

# Explanation

[Reference]

[Lowest Common Ancestor of a Binary Tree - LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/)