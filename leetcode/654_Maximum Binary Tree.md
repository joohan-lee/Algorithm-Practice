# 654. Maximum Binary Tree

Acceptance: 0.8270000000000001
Difficulty: Medium
Skills: BinaryTree
Solved: October 28, 2021

# Description

You are given an integer array `nums` with no duplicates. A **maximum binary tree** can be built recursively from `nums` using the following algorithm:

1. Create a root node whose value is the maximum value in `nums`.
2. Recursively build the left subtree on the **subarray prefix** to the **left** of the maximum value.
3. Recursively build the right subtree on the **subarray suffix** to the **right** of the maximum value.

Return *the **maximum binary tree** built from* `nums`.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/12/24/tree1.jpg](https://assets.leetcode.com/uploads/2020/12/24/tree1.jpg)

```
Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/12/24/tree2.jpg](https://assets.leetcode.com/uploads/2020/12/24/tree2.jpg)

```
Input: nums = [3,2,1]
Output: [3,null,2,null,1]

```

**Constraints:**

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`
- All integers in `nums` are **unique**.

# Solutions

Provide possible solutions in common languages to this problem.

### Python

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        max_val = max(nums)
        max_idx = nums.index(max_val)
        
        l_list = nums[0:max_idx]
        r_list = nums[max_idx+1:]
        n = TreeNode(max_val, self.constructMaximumBinaryTree(l_list), self.constructMaximumBinaryTree(r_list))
        
        return n
```

> Runtime: 196 ms, faster than 89.04% of Python3 online submissions for Maximum Binary Tree.
Memory Usage: 14.6 MB, less than 95.15% of Python3 online submissions for Maximum Binary Tree.
> 

# Complexity Analysis

- Time complexity : O(n^2)*O*(*n*2). The function `construct` is called *n* times. At each level of the recursive tree, we traverse over all the *n* elements to find the maximum element. In the average case, there will be a log*n* levels leading to a complexity of *O*(*n*log*n*). In the worst case, the depth of the recursive tree can grow upto *n*, which happens in the case of a sorted nums*nums* array, giving a complexity of O(n^2).
- Space complexity : *O*(*n*). The size of the *set* can grow upto *n* in the worst case. In the average case, the size will be log*n* for *n* elements in *nums*, giving an average case complexity of *O*(log*n*)

# 해설

해설 참고자료

[Maximum Binary Tree - LeetCode](https://leetcode.com/problems/maximum-binary-tree/solution/)