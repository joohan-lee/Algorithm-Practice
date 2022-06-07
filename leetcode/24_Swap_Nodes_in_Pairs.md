# 24. Swap Nodes in Pairs

Acceptance: 59.0%
Difficulty: Medium
Frequency: 58.19%
Skills: Linked List, Recursion
Solved: June 6, 2022

# Description

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

**Example 1:**

![https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg)

```
Input: head = [1,2,3,4]
Output: [2,1,4,3]

```

**Example 2:**

```
Input: head = []
Output: []

```

**Example 3:**

```
Input: head = [1]
Output: [1]

```

**Constraints:**

- The number of nodes in the list is in the range `[0, 100]`.
- `0 <= Node.val <= 100`

# Solutions

### Python

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cnt = 0
        cur = head
        prev_head = ListNode(-1, head)
        prev = prev_head
        prev_prev = ListNode(-2, prev)
        while cur:
            cnt += 1
					  # Every hitting two elements, swap.
            if cnt % 2 == 0:
								# swap two elements
                temp_next = cur.next
                cur.next = prev
                prev.next = temp_next
                prev_prev.next = cur

                # move cur, prev_prev pointers for the next step
								# cur node and prev node are swapped. So, moving like below:
                prev_prev = cur
                cur = prev.next
            else:
                cur = cur.next
                prev = prev.next
                prev_prev = prev_prev.next
            
        return prev_head.next
```

> Runtime: 40 ms, faster than 60.91% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14 MB, less than 17.63% of Python3 online submissions for Swap Nodes in Pairs.
> 

### Complexity Analysis

- Time complexity : O(N), where N is the size of the linked list.
- Space complexity : O(1)

# Base Idea (One line)

1. Make sure each node points to which node. (Recommend to draw them visually.)

# Explanation

[Reference]

[Swap Nodes in Pairs - LeetCode](https://leetcode.com/problems/swap-nodes-in-pairs/solution/)

1. Recursive
    
    ```python
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def swapPairs(self, head: ListNode) -> ListNode:
            """
            :type head: ListNode
            :rtype: ListNode
            """
    
            # If the list has no node or has only one node left.
            if not head or not head.next:
                return head
    
            # Nodes to be swapped
            first_node = head
            second_node = head.next
    
            # Swapping
            first_node.next  = self.swapPairs(second_node.next)
            second_node.next = first_node
    
            # Now the head is the second node
            return second_node
    ```
    
2. Iterative
    
    ```python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution:
        def swapPairs(self, head: ListNode) -> ListNode:
            """
            :type head: ListNode
            :rtype: ListNode
            """
            # Dummy node acts as the prevNode for the head node
            # of the list and hence stores pointer to the head node.
            dummy = ListNode(-1)
            dummy.next = head
    
            prev_node = dummy
    
            while head and head.next:
    
                # Nodes to be swapped
                first_node = head;
                second_node = head.next;
    
                # Swapping
                prev_node.next = second_node
                first_node.next = second_node.next
                second_node.next = first_node
    
                # Reinitializing the head and prev_node for next swap
                prev_node = first_node
                head = first_node.next
    
            # Return the new head node.
            return dummy.next
    ```