# 142. Linked List Cycle II

Acceptance: 46.2%
Difficulty: Medium
Frequency: 45.16%
Skills: Hash Table, Linked List, Two Pointers
Solved: October 15, 2022

# Description

Given the `head` of a linked list, return *the node where the cycle begins. If there is no cycle, return* `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (**0-indexed**). It is `-1` if there is no cycle. **Note that** `pos` **is not passed as a parameter**.

**Do not modify** the linked list.

**Example 1:**

![https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

```

**Example 3:**

![https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

```

**Constraints:**

- The number of the nodes in the list is in the range `[0, 104]`.
- `105 <= Node.val <= 105`
- `pos` is `1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

# Solutions

### Python

### Hash

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        
        curr = head
        while curr != None and curr not in visited:
            visited.add(curr)
            curr = curr.next
            
        return None if curr == None else curr
```

> Runtime: 100 ms, faster than 46.98% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 18 MB, less than 10.37% of Python3 online submissions for Linked List Cycle II.
> 

### Complexity Analysis

- Time complexity : O(N), where N is the number of nodes
- Space complexity : O(N)

### Python

### Two pointers

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                ptr1 = head
                ptr2 = slow
                while ptr1 != ptr2:
                    ptr1=ptr1.next
                    ptr2=ptr2.next
                return ptr1
            
        
                
        return None
```

- O(N) time , O(1) space

# Base Idea (One line)

1. Using hash, we can recognize re-visiting.

# Explanation

[Reference]

[Linked List Cycle II - LeetCode](https://leetcode.com/problems/linked-list-cycle-ii/solution/)