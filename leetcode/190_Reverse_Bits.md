# 190. Reverse Bits

Acceptance: 51.9%
Difficulty: Medium
Frequency: 49.07%
Skills: Divide and Conquer, bit manipulation
Solved: October 15, 2022
다시풀기: Once

# Description

Reverse bits of a given 32 bits unsigned integer.

**Note:**

- Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using [2's complement notation](https://en.wikipedia.org/wiki/Two%27s_complement). Therefore, in **Example 2** above, the input represents the signed integer `3` and the output represents the signed integer `1073741825`.

**Example 1:**

```
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation:The input binary string00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is00111001011110000010100101000000.

```

**Example 2:**

```
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation:The input binary string11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is10111111111111111111111111111111.

```

**Constraints:**

- The input must be a **binary string** of length `32`

# Solutions

### Python

```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int):
        res, power = 0, 31
        while n > 0:
            res += (n & 1) << power
            n = n >> 1
            power -= 1
            
        return res
```

> Runtime: 56 ms, faster than 57.05% of Python3 online submissions for Reverse Bits.
Memory Usage: 13.8 MB, less than 94.31% of Python3 online submissions for Reverse Bits.
> 

### Complexity Analysis

- Time complexity : O(1)
- Space complexity : O(1)

# Base Idea (One line)

1. bit manipulation

# Explanation

[Reference]

[Reverse Bits - LeetCode](https://leetcode.com/problems/reverse-bits/solution/)