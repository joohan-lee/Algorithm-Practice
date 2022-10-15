# 138. Copy List with Random Pointer

Acceptance: 50.3%
Difficulty: Medium
Frequency: 77.08%
Skills: Hash Table, Linked List
Solved: October 15, 2022

# Description

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a **[deep copy](https://en.wikipedia.org/wiki/Object_copying#Deep_copy)** of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return *the head of the copied linked list*.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

- `val`: an integer representing `Node.val`
- `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

Your code will **only** be given the `head` of the original linked list.

**Example 1:**

![https://assets.leetcode.com/uploads/2019/12/18/e1.png](https://assets.leetcode.com/uploads/2019/12/18/e1.png)

```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

```

**Example 2:**

![https://assets.leetcode.com/uploads/2019/12/18/e2.png](https://assets.leetcode.com/uploads/2019/12/18/e2.png)

```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

```

**Example 3:**

![https://assets.leetcode.com/uploads/2019/12/18/e3.png](https://assets.leetcode.com/uploads/2019/12/18/e3.png)

```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

```

**Constraints:**

- `0 <= n <= 1000`
- `104 <= Node.val <= 104`
- `Node.random` is `null` or is pointing to some node in the linked list.

# Solutions

### Python

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map_new_nodes = {}
        org = head
        org_prev = None
        new_head = None
        new_prev = None
        while org != None:
            
            new = Node(org.val)
            if not new_head:
                new_head = new
            if new_prev:
                new_prev.next = new
                
            map_new_nodes[org] = new
                
            org_prev = org
            org = org.next
            
            new_prev = new
            
            
            
        # connect random points
        curr = head
        new_curr = new_head
        while curr != None:
            if curr.random == None:
                new_curr.random = None
            else:
                new_curr.random = map_new_nodes[curr.random]
                
            curr = curr.next
            new_curr = new_curr.next
        
        return new_head
```

> Runtime: 61 ms, faster than 60.42% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 15 MB, less than 45.91% of Python3 online submissions for Copy List with Random Pointer.
> 

### Complexity Analysis

- Time complexity : O(N), where N is the number of nodes.
- Space complexity : O(N)

# Base Idea (One line)

1. Using a hash, we can store each new node’s address(value) for each original node(key).

# Explanation

[Reference]

[Copy List with Random Pointer - LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer/solution/)

### Recursive way

```python
/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;
    public Node random;

    public Node() {}

    public Node(int _val,Node _next,Node _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
public class Solution {
  // HashMap which holds old nodes as keys and new nodes as its values.
  HashMap<Node, Node> visitedHash = new HashMap<Node, Node>();

  public Node copyRandomList(Node head) {

    if (head == null) {
      return null;
    }

    // If we have already processed the current node, then we simply return the cloned version of
    // it.
    if (this.visitedHash.containsKey(head)) {
      return this.visitedHash.get(head);
    }

    // Create a new node with the value same as old node. (i.e. copy the node)
    Node node = new Node(head.val, null, null);

    // Save this value in the hash map. This is needed since there might be
    // loops during traversal due to randomness of random pointers and this would help us avoid
    // them.
    this.visitedHash.put(head, node);

    // Recursively copy the remaining linked list starting once from the next pointer and then from
    // the random pointer.
    // Thus we have two independent recursive calls.
    // Finally we update the next and random pointers for the new node created.
    node.next = this.copyRandomList(head.next);
    node.random = this.copyRandomList(head.random);

    return node;
  }
}
```