# 234. Palindrome Linked List

Acceptance: 46.9%
Difficulty: Easy
Frequency: 72.26%
Skills: Linked List, Recursion, Stack, Two Pointers
Solved: May 27, 2022

# Description

Given the `head` of a singly linked list, return `true` if it is a palindrome.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)

```
Input: head = [1,2,2,1]
Output: true

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)

```
Input: head = [1,2]
Output: false

```

**Constraints:**

- The number of nodes in the list is in the range `[1, 105]`.
- `0 <= Node.val <= 9`

**Follow up:**

Could you do it in O(n) time and O(1) space?

# Solutions

### Python

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # time: O(n), space: O(n)
        node = head
        len_list = 0
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
            len_list += 1
        
        if len_list % 2 == 1:
            return arr[:(len_list//2)] == arr[(len_list-1):(len_list//2):-1]
        else:
            return arr[:(len_list//2)] == arr[(len_list-1):(len_list//2)-1:-1]
```

> Runtime: 1386 ms, faster than 14.00% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 46.6 MB, less than 48.80% of Python3 online submissions for Palindrome Linked List.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(n)

### Python

O(n), O(1) Using Two Pointers and reverse LinkedList.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # time: O(n), space: O(1)
        # 1. Find the end of the first half using two pointers(slow, fast)
        # 2. Reverse the second half
        # 3. Determine whether or not there is a pailndrome
        # 4. Restore the list (since the function could be part of a bigger program)
        # 5. Return the result
        
        # Find the end of the first half and reverse the second half
        end_pos_first_half = self.find_the_end_of_first_half(head)
        reversed_second_half_start = self.reverse_list(end_pos_first_half.next)
        
        # Check whether or not there's a palindrome
        result = True
        first_pos = head
        second_pos = reversed_second_half_start
        while result and first_pos and second_pos:
            if first_pos.val != second_pos.val:
                result = False
            first_pos = first_pos.next
            second_pos = second_pos.next
        
        # Restore the second half
        end_pos_first_half.next = self.reverse_list(reversed_second_half_start)
        
        return result
        
        
    def find_the_end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # 짝수 개수인 경우: [0,1,2,3] -> [1,2,3]의 1을 반환
        # 홀수 개수인 경우: [0,1,2] -> [1,2]의 1을 반환
        return slow
        
    def reverse_list(self, head):
        prev = None
        cur = head
        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp
        
        return prev
```

> Runtime: 902 ms, faster than 68.91% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 46.9 MB, less than 22.17% of Python3 online submissions for Palindrome Linked List.
> 

### Complexity Analysis

- Time complexity : O(n)
- Space complexity : O(1)

# Base Idea (One line)

1. Copy into Array and then use Two Pointer Technique
2. Reverse second half In-place. **Get the half point of list and reverse the list.**

# Explanation

[Reference]

[Palindrome Linked List - LeetCode](https://leetcode.com/problems/palindrome-linked-list/solution/)