# 547. Number of Provinces

Acceptance: 0.625
Difficulty: Medium
Frequency: 0.3482
Skills: BFS, DFS, Graph, Union Find
Solved: January 27, 2022

# Description

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return *the total number of **provinces***.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)

```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg](https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg)

```
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

```

**Constraints:**

- `1 <= n <= 200`
- `n == isConnected.length`
- `n == isConnected[i].length`
- `isConnected[i][j]` is `1` or `0`.
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]`

# Solutions

### Python

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        startNode = 0
        stack = []
        visited = []
        
        for k in range(n):
            if k not in visited:
                stack.append(k)
                while stack:
                    curNode = stack.pop()
                    if curNode not in visited:
                        visited.append(curNode)
                        for i in range(n):
                            if isConnected[curNode][i] == 1 and curNode != i:
                                stack.append(i) #if curNode and i Node is connected, push it stack
                provinces += 1
        return provinces
```

> Runtime: 208 ms, faster than 59.65% of Python3 online submissions for Number of Provinces.
Memory Usage: 14.3 MB, less than 99.43% of Python3 online submissions for Number of Provinces.
> 

# Complexity Analysis

- Time complexity : For the first for loop, in the worst case such as n provinces, it takes O(n). And then for while loop, in the worst case like only 1 province exists, it takes O(n). For the for loop in while, it takes O(n) to get index of node which is connected. Thus, overall it takes O(n^3).
    - 마지막 for 루프에서 index찾는데 시간을 줄일 수 있을거 같은데..
- Space complexity : I use additional memory for stack and visited. Thus, O(2n) = O(n).

# 해설

해설 참고자료

[Number of Provinces - LeetCode](https://leetcode.com/problems/number-of-provinces/solution/)

## 인접행렬 DFS

괜찮아보이는 풀이가 있어 첨부.

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(c: int):
            for i, v in enumerate(isConnected[c]):
                if not v:
                    continue
                isConnected[c][i] = isConnected[i][c] = 0
                dfs(i)
                
        cnt = 0
        for city, edges in enumerate(isConnected):
            cnt += (sum(edges) >= 1)
            dfs(city)
        return cnt
```

자세해보이는 풀이도 하나 더 첨부.

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # total number of cities
        n = len(isConnected)
        
        if n == 1:
            
            # Quick response for simple case
            return 1
        

        ## View input array as adjacency matrix in graph
        # city <-> node
        # directly connected <-> edge
        adj_matrix = isConnected
        
        
        # DFS helper function to visit all city in the same province (connected component)
        visited = set()
        def visitProvCities(city_idx):
            
            # add current city into visited set
            visited.add(city_idx)
            
            # scan each neighbor city
            for neighbor_city, directly_connected in enumerate(adj_matrix[city_idx]):
                
                if directly_connected and (neighbor_city not in visited):
                            
                    # visit neighbor city in the same province
                    visitProvCities(neighbor_city)
            
            return
        # --------------------------------------------------------
        
        # use helper function to count the number of provinces (i.e., connected component in Graph)
        province_count = 0
        
        for city_idx in range(n):
            
            if city_idx not in visited:
                
                # update province count
                province_count += 1
                
                # start visit all cities of current province
                visitProvCities(city_idx)
        
        
        return province_count
```