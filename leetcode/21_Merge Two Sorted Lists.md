# 21. Merge Two Sorted Lists

Acceptance: 60.4%
Difficulty: Easy
Frequency: 75.41%
Skills: Linked List, Recursion
Solved: May 10, 2022

# Description

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

```

**Example 2:**

```
Input: list1 = [], list2 = []
Output: []

```

**Example 3:**

```
Input: list1 = [], list2 = [0]
Output: [0]

```

**Constraints:**

- The number of nodes in both lists is in the range `[0, 50]`.
- `100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order.

# Solutions

### Python1

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        prev = prehead
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                prev.next = list2
                list2 = list2.next
            else:
                prev.next = list1
                list1 = list1.next
            prev = prev.next
        # 둘 중 하나의 list는 여전히 node를 가지고 있을 수 있음.
				# 주의!!! 하나 뺴먹을 확률 높음
        prev.next = list1 if list1 is not None else list2
        return prehead.next
```

> Runtime: 55 ms, faster than 40.41% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14 MB, less than 33.19% of Python3 online submissions for Merge Two Sorted Lists.
> 

### Complexity Analysis

- Time complexity : O(n+m)
- Space complexity : O(1)

### Python2

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we can split the problem into subproblems as below
        # merge = list1[0] + merge(list1[1:], list2) {list1[0] < list2[0]}
        #         list2[0] + merge(list1, list2[1:]) {otherwise}
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val >= list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
```

> Runtime: 41 ms, faster than 75.97% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14 MB, less than 33.19% of Python3 online submissions for Merge Two Sorted Lists.
> 

### Complexity Analysis

- Time complexity : O(n+m)
- Space complexity : O(n+m), in the worst case, we will call the function recursively at most m+n times. Thus, we need additional space to stack call memory.

# Base Idea (One line)

1. use prehead point and keep tracking of two lists by prev pointer
2. Splitting into subproblems and making a recurrence formula

# Explanation

[Reference]

[Merge Two Sorted Lists - LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/solution/)