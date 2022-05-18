# 897. Increasing Order Search Tree

Acceptance: 78.3%
Difficulty: Easy
Frequency: 55.91%
Skills: Binary Search Tree, BinaryTree, DFS, Stack, Tree
Solved: May 17, 2022

# Description

Given the `root` of a binary search tree, rearrange the tree in **in-order** so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg](https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg)

```
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg](https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg)

```
Input: root = [5,1,7]
Output: [1,null,5,null,7]

```

**Constraints:**

- The number of nodes in the given tree will be in the range `[1, 100]`.
- `0 <= Node.val <= 1000`

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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ret_tree = []
        new_root = None
        prev = None
        def inorderTraversal(root):
            nonlocal prev
            nonlocal new_root
            if root!=None:
                inorderTraversal(root.left)
                node = TreeNode(root.val,None,None)
                # create new root
                if new_root == None:
                    new_root = node
                # if prev node exists, connect current node to previous node
                if prev!=None:
                    prev.right = node
                prev = node
                # ret_tree.append(root.val)
                inorderTraversal(root.right)
        inorderTraversal(root)
        return new_root
```

> Runtime: 40 ms, faster than 25.95% of Python3 online submissions for Increasing Order Search Tree.
Memory Usage: 13.9 MB, less than 39.58% of Python3 online submissions for Increasing Order Search Tree.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

# Base Idea (One line)

1. Inorder traversal 이용

# Explanation

[Reference]

[Increasing Order Search Tree - LeetCode](https://leetcode.com/problems/increasing-order-search-tree/solution/)

```python
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right
```

LeetCode의 솔루션은 파이썬의 yield를 사용함.

yield에 관한 자료

[](https://dojang.io/mod/page/view.php?id=2412)