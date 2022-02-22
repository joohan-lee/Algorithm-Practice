# 121. Best Time to Buy and Sell Stock

- Acceptance: 53.8%
- Frequency : 95.82%
- Difficulty: Easy
- Skills: Array, Dynamic Programming
- Solved: February 22, 2022

# Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

```

**Example 2:**

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

```

**Constraints:**

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

# Solutions

### Python

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if max < prices[j] - prices[i]:
                    max = prices[j] - prices[i]
        return max if max > 0 else 0
```

> Time Limit Exceeded. Brute Force는 불가.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif max_profit < prices[i] - min_price:
                max_profit = prices[i] - min_price
        return max_profit
```

> Runtime: 1218 ms, faster than 65.04% of Python3 online submissions for Best Time to Buy and Sell Stock.
> Memory Usage: 25 MB, less than 91.41% of Python3 online submissions for Best Time to Buy and Sell Stock.

### Complexity Analysis

- Time complexity :  O(n^2) - Brute Force, O(n) - One pass, where n is the length of array.
- Space complexity : O(1). Only two variables are used.

# Base Idea (One line)

1. 우리의 관심사인 Max profit을 가지고 업데이트해주는 것이 중요.

# Explanation

[Reference]

[Best Time to Buy and Sell Stock - LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/)
