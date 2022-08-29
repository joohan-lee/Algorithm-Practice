# 148. Sort List

Acceptance: 53.5%
Difficulty: Medium
Frequency: 48.60%
Skills: Divide and Conquer, Linked List, Merge Sort, Sorting, Two Pointers
Solved: August 28, 2022
다시풀기: Required

# Description

Given the `head` of a linked list, return *the list after sorting it in **ascending order***.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg](https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg)

```
Input: head = [4,2,1,3]
Output: [1,2,3,4]

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg](https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg)

```
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

```

**Example 3:**

```
Input: head = []
Output: []

```

**Constraints:**

- The number of nodes in the list is in the range `[0, 5 * 104]`.
- `105 <= Node.val <= 105`

**Follow up:** Can you sort the linked list in `O(n logn)` time and `O(1)` memory (i.e. constant space)?

# Solutions

### Python

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Merge Sort -> O(nlogn) time / O(1) space 가능할듯
        if not head:
            return head
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        arr.sort()
        new_head = ListNode()
        head = ListNode(arr[0])
        prev = head
        for i in range(1,len(arr)):
            curr = ListNode(arr[i])
            prev.next = curr
            prev = curr
            
        
        return head
```

> Runtime: 538 ms, faster than 84.45% of Python3 online submissions for Sort List.
Memory Usage: 45.1 MB, less than 9.80% of Python3 online submissions for Sort List.
> 

### Complexity Analysis

- Time complexity : O(nlogn)
- Space complexity : O(n)

### 2. MergeSort (O(nlogn) time, O(1) space)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Merge Sort -> O(nlogn) time / O(1) space 가능할듯
        if head == None or head.next == None:
            return head
        
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def merge(self, list1, list2):
        dummyHead = ListNode()
        ptr = dummyHead
        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        
        if list1:
            ptr.next = list1
        else:
            ptr.next = list2
        
        return dummyHead.next
    
    def getMid(self, head):
        midPrev = None
        while head and head.next:
            midPrev = head if (midPrev == None) else midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        
        return mid
```

# Base Idea (One line)

1. Sort and convert list to linkedlist
2. Use Merge Sort

# Explanation

[Reference]

[Sort List - LeetCode](https://leetcode.com/problems/sort-list/solution/)