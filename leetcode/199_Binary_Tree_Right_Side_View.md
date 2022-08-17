# 199. Binary Tree Right Side View

Acceptance: 60.9%
Difficulty: Medium
Frequency: 73.88%
Skills: BFS, BinaryTree, DFS, Tree
Solved: August 16, 2022

# Description

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/14/tree.jpg](https://assets.leetcode.com/uploads/2021/02/14/tree.jpg)

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

```

**Example 2:**

```
Input: root = [1,null,3]
Output: [1,3]

```

**Example 3:**

```
Input: root = []
Output: []

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return []
        curr_q = deque([root])
        next_q = deque()
        while curr_q or next_q:
            node = curr_q.popleft()
            
            if node.left:
                next_q.append(node.left)
            if node.right:
                next_q.append(node.right)
            if len(curr_q) == 0:
                ans.append(node.val)
                curr_q = next_q
                next_q = deque()
        return ans
```

> Runtime: 49 ms, faster than 58.81% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 13.8 MB, less than 70.69% of Python3 online submissions for Binary Tree Right Side View.
> 

### Complexity Analysis

- Time complexity : O(N) since one has to visit each node
- Space complexity : O(D) to keep the queues, where D is a tree diameter.

# Base Idea (One line)

1. Use two queues to figure out when level is changed while BFS so that collect all right-most values

# Explanation

[Reference]

[Binary Tree Right Side View - LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/solution/)