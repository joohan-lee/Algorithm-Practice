# 141. Linked List Cycle

Acceptance: 46.0%
Difficulty: Easy
Frequency: 60.81%
Skills: Hash Table, Linked List, Two Pointers
Solved: May 22, 2022

# Description

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

**Example 1:**

![https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

```

**Example 2:**

![https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

```

**Example 3:**

![https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

```

**Constraints:**

- The number of the nodes in the list is in the range `[0, 104]`.
- `105 <= Node.val <= 105`
- `pos` is `1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

# Solutions

### Python

Using Hash Table (or you can use HashSet)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash = {}
        cur = head
        # hash에 cur.val만을 저장하면 중복 value가 있을때 처리가 안됨.
        # 그렇다고 hash의 key를 node로 이용하는건 뭔가 오류를 일으킬 것 같다..
        # hash와 유사한 파이썬의 set을 이용하여 방문한 node를 보관하는게 좋을 듯.
        while cur:
            if cur in hash:
                return True
            else:
                hash[cur] = 1
            
            cur = cur.next
        
        return False
```

> Runtime: 88 ms, faster than 31.09% of Python3 online submissions for Linked List Cycle.
Memory Usage: 18 MB, less than 10.02% of Python3 online submissions for Linked List Cycle.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

### Python

Two Pointers(Floyd’s Cycle Finding Algorithm)

**Intuition:** Imagine two runners running on a track at different speed. What happens when the track is actually a circle?

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Imagine two runners running on a track at different speed. What happens when the track is actually a circle?
        if head == None:
            return False
        slow = head
        fast = head.next
        
        # keep visiting next node until both pointers are same
        while slow != fast:
            # if there is tail and null node, return False
            # We should check fast node and fast.next is not null in order to move
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
```

> Runtime: 63 ms, faster than 71.74% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.6 MB, less than 66.65% of Python3 online submissions for Linked List Cycle.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(1)

# Base Idea (One line)

1. Check if the node is visited using HashSet.
2. Floyd’s Cycle Finding Algorithm(Two Pointers)

# Explanation

[Reference]

[Linked List Cycle - LeetCode](https://leetcode.com/problems/linked-list-cycle/solution/)