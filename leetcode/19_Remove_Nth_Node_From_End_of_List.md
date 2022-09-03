# 19. Remove Nth Node From End of List

Acceptance: 39.1%
Difficulty: Medium
Frequency: 66.30%
Skills: Linked List, Two Pointers
Solved: September 1, 2022

# Description

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

```

**Example 2:**

```
Input: head = [1], n = 1
Output: []

```

**Example 3:**

```
Input: head = [1,2], n = 1
Output: [1]

```

**Constraints:**

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

**Follow up:** Could you do this in one pass?

# Solutions

### Python

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        gap = 0
        while gap < n:
            first = first.next
            gap += 1
        
        dummyHead = ListNode(next=head)
        prev_second = dummyHead
        while first:
            first = first.next
            prev_second = prev_second.next
            second = second.next
        
        prev_second.next = second.next
        
        return dummyHead.next
```

> Runtime: 45 ms, faster than 69.35% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.8 MB, less than 70.27% of Python3 online submissions for Remove Nth Node From End of List.
> 

### Complexity Analysis

- Time complexity : O(N), where N is the number of nodes
- Space complexity : O(1)

# Base Idea (One line)

1. Two pointers with n gaps

# Explanation

[Reference]

[Remove Nth Node From End of List - LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/)