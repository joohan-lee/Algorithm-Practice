# 208. Implement Trie (Prefix Tree)

Acceptance: 60.0%
Difficulty: Medium
Frequency: 62.13%
Skills: Design, Hash Table, String, Trie
Solved: August 21, 2022

# Description

A **[trie](https://en.wikipedia.org/wiki/Trie)** (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

**Example 1:**

```
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

```

**Constraints:**

- `1 <= word.length, prefix.length <= 2000`
- `word` and `prefix` consist only of lowercase English letters.
- At most `3 * 104` calls **in total** will be made to `insert`, `search`, and `startsWith`.

# Solutions

### Python

```python
class Node(object):
        def __init__(self, key, isEnd = False):
            self.key = key
            self.isEnd = isEnd
            self.child = {}
class Trie:
    def __init__(self):
        self.root = Node(None)
        

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.child:
                curr_node.child[char] = Node(char)
            curr_node = curr_node.child[char]
        curr_node.isEnd = True
        
        return None
        

    def search(self, word: str) -> bool:
        curr_node = self.root
        for char in word:
            if char not in curr_node.child:
                return False
            curr_node = curr_node.child[char]
        
        if curr_node.isEnd:
            return True
        

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.child:
                return False
            curr_node = curr_node.child[char]
        
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

> Runtime: 307 ms, faster than 39.00% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 31.5 MB, less than 72.93% of Python3 online submissions for Implement Trie (Prefix Tree).
> 

### Complexity Analysis

- Time complexity : Let L is the length of string.
    - insert: O(L)
    - search: O(L)
    - startswith: O(L)
- Space complexity : Let L is the length of string.
    - insert: O(L)
    - search: O(1)
    - startswith: O(1)

# Base Idea (One line)

1. Implementing Trie

# Explanation

[Reference]

[Implement Trie (Prefix Tree) - LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/solution/)

Refer this [link](https://velog.io/@kimdukbae/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8A%B8%EB%9D%BC%EC%9D%B4-Trie) for more information about Trie.