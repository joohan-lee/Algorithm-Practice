# 226. Invert Binary Tree

Acceptance: 0.7070000000000001
Difficulty: Easy
Frequency: 0.4238
Skills: BFS, BinaryTree, DFS, Tree
Solved: February 3, 2022

# Description

Given the `root` of a binary tree, invert the tree, and return *its root*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

```
Input: root = [2,1,3]
Output: [2,3,1]

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # swap left to right during dfs
        stack, visited = [], []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            if node not in visited and node != None:
                # 비어있는 root 혹은 leaf 노드인 경우 진행하지 않기 위함
                # swap(invert)
                node.left, node.right = node.right, node.left
                
                    
                # add node to visited
                visited.append(node)
                # add adjacent nodes to stack (left, right node is adjacent)
                stack.append(node.left)
                stack.append(node.right)
        return root
```

> Runtime: 47 ms, faster than 32.70% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14 MB, less than 88.68% of Python3 online submissions for Invert Binary Tree.
> 

# Complexity Analysis

- Time complexity : Since we visit all nodes, the time complexity takes O(n), where n is the number of nodes in the tree.
- Space complexity : Space complexity is O(n).

![Untitled](226%20Invert%20Binary%20Tree%20e916cd889a294aeeb94db93d9312708f/Untitled.png)

# 해설

해설 참고자료

[Invert Binary Tree - LeetCode](https://leetcode.com/problems/invert-binary-tree/solution/)