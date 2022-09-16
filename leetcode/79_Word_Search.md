# 79. Word Search

Acceptance: 40.0%
Difficulty: Medium
Frequency: 88.64%
Skills: Array, Backtracking, Matrix
Solved: September 15, 2022
다시풀기: Required

# Description

Given an `m x n` grid of characters `board` and a string `word`, return `true` *if* `word` *exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/11/04/word2.jpg](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

```

**Example 3:**

![https://assets.leetcode.com/uploads/2020/10/15/word3.jpg](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

```

**Constraints:**

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.

**Follow up:** Could you use search pruning to make your solution faster with a larger `board`?

# Solutions

### Python

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set() # path we visited
        
        def dfs(r,c,i):
            if i == len(word):
                # if we found all characters in word
                return True
            if r<0 or c <0 or r >=ROWS or c>= COLS or word[i] != board[r][c] or (r,c) in path:
                return False

            path.add((r,c))
            res = (dfs(r+1,c,i+1) or\
                   dfs(r-1,c,i+1) or\
                   dfs(r,c+1,i+1) or\
                   dfs(r,c-1,i+1))
            
            # for k, l in [(0,1), (0,-1), (1,0), (-1,0)]:
            #     # if any neigbor node is True, res == True
            #     res = res or (dfs(r+k, c+l, i+1))

            path.remove((r,c))

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False
```

> Runtime: Time Limit Exceeded
Memory Usage:
> 

### Complexity Analysis

- Time complexity : O(m * n * 4^len(word))
- Space complexity : O(L) where L is the length of the word to be matched
    - The main consumption of the memory lies in the recursion call of the backtracking function. The maximum length of the call stack would be the length of the word. Therefore, the space complexity of the algorithm is O(*L*).

# Base Idea (One line)

1. DFS and Backtracking

# Explanation

[Reference]

[Word Search - LeetCode](https://leetcode.com/problems/word-search/solution/)

DFS

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        directions = [(0,1), (0,-1),(1,0),(-1,0)]
        result = False
        def dfs(i,r,c):
            nonlocal result
            nonlocal visited
            if i == len(word) - 1:
                return True
            # print("!!", r,c,i)
            for direction in directions:
                nr = r + direction[0]
                nc = c + direction[1]
                if nr >= 0 and nr < m and nc >= 0 and nc < n and board[nr][nc] == word[i+1] and (nr,nc) not in visited:
                    # print(nr,nc,i)
                    visited.add((nr,nc))
                    result = dfs(i + 1, nr, nc)
                    visited.remove((nr,nc))
                    # print(result)
                    
            return result
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    visited = {(r,c)}
                    result = dfs(0,r,c)
                    if result:
                        return True
        
        return result
```

O(m*n*4^(len(word))

해설코드

```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False

    
    def backtrack(self, row, col, suffix):
        """
            backtracking with side-effect,
               the matched letter in the board would be marked with "#".
        """
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            # sudden-death return, no cleanup.
            if self.backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                return True

        # revert the marking
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return False
```

Backtracking template이 있다

[https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2793/](https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2793/)

```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
```