# 105. Construct Binary Tree from Preorder and Inorder Traversal

Acceptance: 60.0%
Difficulty: Medium
Frequency: 62.23%
Skills: Array, BinaryTree, Divide and Conquer, Hash Table, Tree
Solved: August 18, 2022
다시풀기: Required

# Description

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return *the binary tree*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/19/tree.jpg](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

```

**Example 2:**

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]

```

**Constraints:**

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of **unique** values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is **guaranteed** to be the preorder traversal of the tree.
- `inorder` is **guaranteed** to be the inorder traversal of the tree.

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def arrayToTree(left, right):
            nonlocal preorder_idx
            if left > right:
                return None
            
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            
            preorder_idx += 1
            
            root.left = arrayToTree(left, inorder_hash[root_val] - 1)
            root.right = arrayToTree(inorder_hash[root_val] + 1, right)
            
            return root
            
            
        preorder_idx = 0
        inorder_hash = {}
        for idx, val in enumerate(inorder):
            inorder_hash[val] = idx
        
        return arrayToTree(0,len(preorder)-1)
```

> Runtime: 100 ms, faster than 79.12% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 18.9 MB, less than 86.54% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
> 

### Complexity Analysis

Let N*N* be the length of the input arrays.

- Time complexity : *O*(*N*).
    
    Building the hashmap takes *O*(*N*) time, as there are *N* nodes to add, and adding items to a hashmap has a cost of *O*(1), so we get *N*⋅*O*(1)=*O*(*N*).
    
    Building the tree also takes *O*(*N*) time. The recursive helper method has a cost of *O*(1) for each call (it has no loops), and it is called *once* for each of the *N* nodes, giving a total of *O*(*N*).
    
    Taking both into consideration, the time complexity is *O*(*N*).
    
- Space complexity : *O*(*N*).
    
    Building the hashmap and storing the entire tree each requires *O*(*N*) memory. The size of the implicit system stack used by recursion calls depends on the height of the tree, which is *O*(*N*) in the worst case and *O*(log*N*) on average. Taking both into consideration, the space complexity is *O*(*N*).
    

# Base Idea (One line)

1. The list, preorder, represents sequentially each root of subtrees. Recursively construct tree with hash table to access root value in constant time.

# Explanation

[Reference]

[Construct Binary Tree from Preorder and Inorder Traversal - LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/)