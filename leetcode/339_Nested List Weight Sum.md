# 339. Nested List Weight Sum

Acceptance: 0.8
Difficulty: Medium
Frequency: 0.7532
Skills: BFS, DFS
Solved: February 3, 2022
다시풀기: Required

# Description

You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists.

The **depth** of an integer is the number of lists that it is inside of. For example, the nested list `[1,[2,2],[[3],2],1]` has each integer's value set to its **depth**.

Return *the sum of each integer in* `nestedList` *multiplied by its **depth***.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/01/14/nestedlistweightsumex1.png](https://assets.leetcode.com/uploads/2021/01/14/nestedlistweightsumex1.png)

```
Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/01/14/nestedlistweightsumex2.png](https://assets.leetcode.com/uploads/2021/01/14/nestedlistweightsumex2.png)

```
Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
```

**Example 3:**

```
Input: nestedList = [0]
Output: 0

```

**Constraints:**

- `1 <= nestedList.length <= 50`
- The values of the integers in the nested list is in the range `[-100, 100]`.
- The maximum **depth** of any integer is less than or equal to `50`.

# Solutions

### Python

DFS 혹은 BFS를 주어진 Interface를 이용하여 수행하는게 중요했다.

(nestedList 의 요소인 NestedInteger는 a single integer일 수도 있고 a nested list일 수도 있다.)

**nested니까 우선은 recursive로 풀 수 있고, 때문에 dfs로 구현할 수 있다.**

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        def dfs(nested_list, depth):
            sum = 0
            for nested in nested_list:
                if nested.isInteger() == True:
                    sum += nested.getInteger() * depth
                else:
                    sum += dfs(nested.getList(), depth+1)
            
            return sum
        
        return dfs(nestedList, 1)
```

> Runtime: 72 ms, faster than 5.77% of Python3 online submissions for Nested List Weight Sum.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Nested List Weight Sum.
> 

# Complexity Analysis

Let *N* be the total number of nested elements in the input list. For example, the list `[ [[[[1]]]], 2 ]` contains 4 nested lists and 2 nested integers (1 and 2), so *N*=6 for that particular case.

- Time complexity : O(*N*).
    
    Recursive functions can be a bit tricky to analyze, particularly when their implementation includes a loop. A good strategy is to start by determining how many times the recursive function is called, and then how many times the loop will iterate *across all calls to the recursive function*.
    
    The recursive function, `dfs(...)` is called exactly **once** for each *nested list*. As *N* also includes nested integers, we know that the number of recursive calls has to be *less than N*.
    
    On each nested list, it iterates over all of the nested elements **directly inside that list** (in other words, not nested further). As each nested element can only be directly inside **one** list, we know that there must only be one loop iteration *for each nested element*. This is a total of *N* loop iterations.
    
    So combined, we are performing at most 2⋅*N* recursive calls and loop iterations. We drop the 2 as it is a constant, leaving us with time complexity O(*N*).
    
- Space complexity : O(*N*).
    
    In terms of space, at most *O*(*D*) recursive calls are placed on the stack, where *D* is the maximum level of nesting in the input. For example, *D*=2 for the input `[[1,1],2,[1,1]]`, and *D*=3 for the input `[1,[4,[6]]]`.
    
    In the worst case, *D*=*N*, (e.g. the list `[[[[[[]]]]]]`) so the worst-case space complexity is *O*(*N*).
    

# 해설

해설 참고자료

[Account Login - LeetCode](https://leetcode.com/problems/nested-list-weight-sum/solution/)

BFS로 푸는 방법

```python
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        queue = deque(nestedList)

        depth = 1
        total = 0

        while len(queue) > 0:
            for i in range(len(queue)):
                nested = queue.pop()
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    queue.extendleft(nested.getList())
            depth += 1

        return total
```

BFS는 list 전체적으로 탐색하며 다 더하고 nested를 하나씩 벗겨나가며 계속 더하는 느낌이다.

[DFS 완벽 구현하기 - 파이썬](https://data-marketing-bk.tistory.com/44)

재귀로 dfs 구현 연습이 필요해보인다.
