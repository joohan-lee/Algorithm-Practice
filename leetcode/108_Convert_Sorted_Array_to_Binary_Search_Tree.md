# 108. Convert Sorted Array to Binary Search Tree

Acceptance: 68.7%
Difficulty: Easy
Frequency: 58.87%
Skills: Array, Binary Search Tree, BinaryTree, Divide and Conquer, Tree
Solved: September 18, 2022

# Description

Given an integer array `nums` where the elements are sorted in **ascending order**, convert *it to a **height-balanced** binary search tree*.

A **height-balanced** binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)

```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

```

![https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg](https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg)

**Example 2:**

![https://assets.leetcode.com/uploads/2021/02/18/btree.jpg](https://assets.leetcode.com/uploads/2021/02/18/btree.jpg)

```
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

```

**Constraints:**

- `1 <= nums.length <= 104`
- `104 <= nums[i] <= 104`
- `nums` is sorted in a **strictly increasing** order.

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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # [-10, -3, 0, 5, 9]
        # 0: root, [-10, -3]: left-subtree, [5,9]: right-subtree
        # left / -10: root, -3: right-subtree
        # right / 5: root, 9: right-subtree
        def buildBST(arr: List[int]) -> Optional[TreeNode]:
            if len(arr) == 0:
                return None
            left = 0
            right = len(arr) - 1
            mid = left + (right - left) // 2
            
            root = TreeNode(arr[mid])
            root.left = buildBST(arr[left:mid])
            root.right = buildBST(arr[mid+1:right+1])
            
            return root
        
        return buildBST(nums)
    
    # [-10, -3, 0, 5, 9]
    # left: 0 , right: 4, mid: 2, root: 0
    # arr: [-10, -3], left: 0, right: 1, mid: 0, root: -10
    # arr: [], return None
    # arr: [-3], left: 0, right: 0, mid: 0, root: -3
    # arr: [5,9], left: 0, right: 1, mid: 0, root: 5
    # arr: [], return None
    # arr: [9], left: 0, right: 0, mid: 0, root: 9
    
    #    0
    # -10   5
    #_  -3 _ 9
```

> Runtime: 
Memory Usage:
> 

### Complexity Analysis

- Time complexity : O(N) where N is the number of nodes
- Space complexity : O(logN). The recursion stack requires O(logN) space because the tree is height-balanced.

# Base Idea (One line)

1. Recursively preorder traversal root, left-subtree, right-subtree and connect them.

# Explanation

[Reference]

[Convert Sorted Array to Binary Search Tree - LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solution/)