# 114. Flatten Binary Tree to Linked List

Acceptance: 60.4%
Difficulty: Medium
Frequency: 52.98%
Skills: BinaryTree, DFS, Linked List, Stack, Tree
Solved: August 5, 2022

# Description

Given the `root` of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
- The "linked list" should be in the same order as a **[pre-order traversal](https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR)** of the binary tree.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg](https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg)

```
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

```

**Example 2:**

```
Input: root = []
Output: []

```

**Example 3:**

```
Input: root = [0]
Output: [0]

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def help(curr):
            if curr == None:
                return
            help(curr.left)
            help(curr.right)

            if curr.left:
                temp = curr.right
                curr.right = curr.left
                curr.left = None
                while curr.right != None:
                    curr = curr.right
                curr.right = temp
                
        
        help(root)
```

> Runtime: 72 ms, faster than 22.45% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 15.3 MB, less than 48.54% of Python3 online submissions for Flatten Binary Tree to Linked List.
> 

### Complexity Analysis

- Time complexity : O(N)
- Space complexity : O(N) which is occupied by recursion stack

# Base Idea (One line)

1. Recursion

# Explanation

[Reference]

[Flatten Binary Tree to Linked List - LeetCode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solution/)