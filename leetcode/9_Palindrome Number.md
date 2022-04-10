# 9. Palindrome Number

Acceptance: 0.523
Difficulty: Medium
Frequency: 0.8527
Skills: Math
Solved: April 10, 2022

# Description

Given an integer `x`, return `true` if `x` is palindrome integer.

An integer is a **palindrome** when it reads the same backward as forward.

- For example, `121` is a palindrome while `123` is not.

**Example 1:**

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

```

**Example 2:**

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```

**Example 3:**

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

```

**Constraints:**

- `231 <= x <= 231 - 1`

# Solutions

### Python

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reverse = s[::-1]
        return s == reverse
```

> Runtime: 56 ms, faster than 94.75% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.8 MB, less than 64.12% of Python3 online submissions for Palindrome Number.
> 

### Complexity Analysis

- Time complexity : O(n), where n is the total digit of given x.
- Space complexity : O(n)

# Base Idea (One line)

1. Are numbers same when it is reversed and not?

# Explanation

[Reference]

```python
public class Solution {
    public bool IsPalindrome(int x) {
        // Special cases:
        // As discussed above, when x < 0, x is not a palindrome.
        // Also if the last digit of the number is 0, in order to be a palindrome,
        // the first digit of the number also needs to be 0.
        // Only 0 satisfy this property.
        if(x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int revertedNumber = 0;
        while(x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }

        // When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        // For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        // since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
        return x == revertedNumber || x == revertedNumber/10;
    }
}
```

number에 대한 palindrome이므로 string보다 빠르게 구할 수 있다. O(log_10(n))(time)/O(1)(space)으로 가능.

일의 자리부터 10의 나눗셈 나머지를 구하여 역으로 숫자를 만들어서 계산.