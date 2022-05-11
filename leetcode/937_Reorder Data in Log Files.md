# 937. Reorder Data in Log Files

Acceptance: 56.0%
Difficulty: Easy
Frequency: 76.61%
Skills: Array, Sorting, String
Solved: May 11, 2022

# Description

You are given an array of `logs`. Each log is a space-delimited string of words, where the first word is the **identifier**.

There are two types of logs:

- **Letter-logs**: All words (except the identifier) consist of lowercase English letters.
- **Digit-logs**: All words (except the identifier) consist of digits.

Reorder these logs so that:

1. The **letter-logs** come before all **digit-logs**.
2. The **letter-logs** are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
3. The **digit-logs** maintain their relative ordering.

Return *the final order of the logs*.

**Example 1:**

```
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

```

**Example 2:**

```
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

```

**Constraints:**

- `1 <= logs.length <= 100`
- `3 <= logs[i].length <= 100`
- All the tokens of `logs[i]` are separated by a **single** space.
- `logs[i]` is guaranteed to have an identifier and at least one word after the identifier.

# Solutions

### Python

```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_log = []
        dig_log = []
        for string in logs:
            s = string.split(' ')
            if s[1].isdigit():
                dig_log.append(s)
            else:
                let_log.append(s)
        
       
        for i in range(0, len(let_log)-1):
            for j in range(0, len(let_log)-i-1):
                s1 = ' '.join(let_log[j][1:])
                s2 = ' '.join(let_log[j+1][1:])
                if s1 > s2 or (s1 == s2 and let_log[j][0] > let_log[j+1][0]):
                    let_log[j], let_log[j+1] = let_log[j+1], let_log[j]
                    

        ret = []
        for arr in let_log:
            ret.append(' '.join(arr))
        for arr in dig_log:
            ret.append(' '.join(arr))
        return ret
```

> Runtime: 59 ms, faster than 32.37% of Python3 online submissions for Reorder Data in Log Files.
Memory Usage: 14.1 MB, less than 7.85% of Python3 online submissions for Reorder Data in Log Files.
> 

### Complexity Analysis

- Time complexity : O(n^2) , bubble sorting
- Space complexity : O(n)

# Base Idea (One line)

1. Sorting을 구현하여 새로이 배열을 sorting하는 방법
2. 사용자 정의 정렬(**custom sort**)

# Explanation

위에서 나는 직접 string을 비교하여 bubble sortind을 구현하였지만, 파이썬 자체를 custom sort할 수 있다.

```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)
```

참고로, 두 개 이상의 조건으로 sort이용할 시 아래처럼 이용할 수 있다.

```python
# 1번 값을 기준으로 정렬하고, 동일 값은 0번 값을 기준으로 정렬하려는 경우 아래처럼 할 수 있음.
array.sort(key=lambda x: (x[1], x[0]))

#비슷하게 위 solution 코드에서 rest[0]가 alphabet이면 0순위로 정렬되고 
# 그 뒤는 rest에 따라서, 그 후에도 같은 값은 _id를 기준으로 정렬된다.
return (0, rest, _id) if rest[0].isalpha() else (1, )
```

[Reference]

[Reorder Data in Log Files - LeetCode](https://leetcode.com/problems/reorder-data-in-log-files/solution/)