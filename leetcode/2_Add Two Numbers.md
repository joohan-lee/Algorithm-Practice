# 2. Add Two Numbers

Acceptance: 38.8%
Difficulty: Medium
Frequency: 94.01%
Skills: Linked List, Math, Recursion
Solved: May 30, 2022

# Description

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

```

**Example 2:**

```
Input: l1 = [0], l2 = [0]
Output: [0]

```

**Example 3:**

```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

```

**Constraints:**

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

# Solutions

### Python

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummyHead = ListNode(0)
        cur = dummyHead
        while l1 and l2:
            n = l1.val + l2.val + carry
            if n >= 10:
                n %= 10
                node = ListNode(n)
                carry = 1
            else:
                node = ListNode(n)
                carry = 0
            cur.next = node
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            n = l1.val + carry
            if n >= 10:
                n %= 10
                carry = 1
                node = ListNode(n)
            else:
                carry = 0
                node = ListNode(n)
            cur.next = node
            cur = cur.next
            l1 = l1.next
        while l2:
            n = l2.val + carry
            if n >= 10:
                n %= 10
                carry = 1
                node = ListNode(n)
            else:
                carry = 0
                node = ListNode(n)
            cur.next = node
            cur = cur.next
            l2 = l2.next
        if carry == 1:
            node = ListNode(carry)
            cur.next = node
        
            
        return dummyHead.next
```

> Runtime: 123 ms, faster than 19.13% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 44.00% of Python3 online submissions for Add Two Numbers.
> 

### Complexity Analysis

- Time complexity : O(max(m,n))
- Space complexity : O(1), if the return list does not count towards space complexity. If it does, O(max(m,n)), since the length of new list is at most max(m,n) + 1.

# Base Idea (One line)

1. Keep adding two elements and handle carry.

# Explanation

[Reference]

[Add Two Numbers - LeetCode](https://leetcode.com/problems/add-two-numbers/solution/)

I can make my solution shorter.

```python
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummyHead = new ListNode(0);
    ListNode p = l1, q = l2, curr = dummyHead;
    int carry = 0;
    while (p != null || q != null) {
        int x = (p != null) ? p.val : 0;
        int y = (q != null) ? q.val : 0;
        int sum = carry + x + y;
        carry = sum / 10;
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        if (p != null) p = p.next;
        if (q != null) q = q.next;
    }
    if (carry > 0) {
        curr.next = new ListNode(carry);
    }
    return dummyHead.next;
}
```