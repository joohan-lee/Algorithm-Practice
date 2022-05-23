# 112. Path Sum

Acceptance: 45.6%
Difficulty: Easy
Frequency: 44.12%
Skills: BFS, BinaryTree, DFS, Tree
Solved: May 20, 2022

# Description

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg](https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg)

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

```
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

```

**Example 3:**

```
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5000]`.
- `1000 <= Node.val <= 1000`
- `1000 <= targetSum <= 1000`

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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result = False
        def helper(node, currentSum):
            nonlocal result
            currentSum += node.val
            
            # when node is a leaf node, check currentSum is equal to targetSum
            if node.left == None and node.right == None:
                if currentSum == targetSum:
                    result = True
            
            # visit children recursively
            if node.left:
                helper(node.left, currentSum)
            if node.right:
                helper(node.right, currentSum)
        
        if root:
            helper(root, 0)
        else:
            result = False
        
        return result
```

> Runtime: 61 ms, faster than 44.02% of Python3 online submissions for Path Sum.
Memory Usage: 14.9 MB, less than 93.24% of Python3 online submissions for Path Sum.
> 

### Complexity Analysis

- Time complexity : O(n), where n is the number of nodes because we should search all nodes
- Space complexity : O(n), because we call helper function n times

# Base Idea (One line)

1. DFS or BFS using top-down recursion
2. DFS or BFS using stack or queue respectively

# Explanation

[Reference]

Recursion

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case
        if not root:
            return False
        
        targetSum -= root.val
        # if it is a leaf node, check sum == 0
        if root.left == None and root.right == None:
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
```

Iteration

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, targetSum - root.val)]
        
        while stack:
            node, remainSum = stack.pop()
            
            # if node is a leaf node, check remaining sum is 0
            if node.left == None and node.right == None:
                if remainSum == 0:
                    return True
            
            if node.left:
                stack.append((node.left, remainSum - node.left.val))
            if node.right:
                stack.append((node.right, remainSum - node.right.val))
        
        return False
```

[Path Sum - LeetCode](https://leetcode.com/problems/path-sum/solution/)