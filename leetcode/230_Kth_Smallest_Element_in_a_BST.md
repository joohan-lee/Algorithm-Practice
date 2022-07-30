# Template

Acceptance: 68.5%
Difficulty: Medium
Frequency: 55.73%
Skills: Binary Search Tree, BinaryTree, DFS, Tree
Solved: July 30, 2022

# Description

Given the `root` of a binary search tree, and an integer `k`, return *the* `kth` *smallest value (**1-indexed**) of all the values of the nodes in the tree*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

```
Input: root = [3,1,4,null,2], k = 1
Output: 1

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

```

**Constraints:**

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 104`
- `0 <= Node.val <= 104`

**Follow up:** If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def postorder(curr):
            if curr.right != None:
                postorder(curr.right)
            arr.append(curr.val)
            if curr.left != None:
                postorder(curr.left)
            
        
        arr = []
        postorder(root)
        
        return arr[-k]
```

> Runtime: 94 ms, faster than 29.92% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18.1 MB, less than 14.22% of Python3 online submissions for Kth Smallest Element in a BST.
> 

### Complexity Analysis

- Time complexity : O(n), where n is the number of nodes
- Space complexity : O(n) for arr

# Base Idea (One line)

1. Inorder traverse

# Explanation

[Reference]

[Kth Smallest Element in a BST - LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/)