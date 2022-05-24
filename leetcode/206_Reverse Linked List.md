# 206. Reverse Linked List

Acceptance: 70.5%
Difficulty: Easy
Frequency: 67.68%
Skills: Linked List, Recursion
Solved: May 23, 2022

# Description

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

```
Input: head = [1,2]
Output: [2,1]

```

**Example 3:**

```
Input: head = []
Output: []

```

**Constraints:**

- The number of nodes in the list is the range `[0, 5000]`.
- `5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

# Solutions

### Python

Iterative

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp
        return prev
```

> Runtime: 51 ms, faster than 45.43% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.5 MB, less than 56.32% of Python3 online submissions for Reverse Linked List.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(1)

### Python

Recursive

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        
        p = self.reverseList(head.next) # 현재까지 생성한 리스트
        head.next.next = head # head의 다음노드는 나를 가리킨다
        head.next = None # 원본 리스트에서 나 이후로는 연결 끊기(재귀로 연결되어있으므로 상관X)

        return p
```

위의 재귀는 솔루션에 있는 방식인데 뭔가 이해하기 좀 어려워서 아래처럼 다시 구현하였다. (성능은 위 솔루션이 더 좋았음)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(prev: ListNode, cur: ListNode):
            if not cur:
                return prev
            
            next_temp = cur.next
            cur.next = prev
            return helper(cur, next_temp)
        
        return helper(None, head)
```

> Runtime: 41 ms, faster than 73.74% of Python3 online submissions for Reverse Linked List.
Memory Usage: 20.4 MB, less than 17.37% of Python3 online submissions for Reverse Linked List.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

# Base Idea (One line)

1. reverse the link with temporary variable for link

# Explanation

[Reference]

[Reverse Linked List - LeetCode](https://leetcode.com/problems/reverse-linked-list/solution/)