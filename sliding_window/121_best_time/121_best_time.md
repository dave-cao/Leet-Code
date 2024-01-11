---
tag: code_problem
time_elapsed: 49
difficulty: easy
created: 2024-01-10T14:24
updated: 2024-01-10T17:14
---

# 121 Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
This is a sliding window / two-pointer question. We first have to realize that this only goes in one direction. 

# Approach
<!-- Describe your approach to solving the problem. -->
I have two pointers, a left and right index. If we ever get a negative profit, that means the right index is less than the right index, so we update the left index to be the right index. If it isn't, then the left index is still the lowest so far, and we can update the right index one more to the right. We can check for maxes. At the end, we return the max profit

# Complexity
- Time complexity: $O(n)$

- Space complexity: $O(1)$

# Code
```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        left_index = 0
        right_index = 1
        max_profit = 0
        while right_index < len(prices):
            profit = prices[right_index] - prices[left_index]

            if profit < 0:
                left_index = right_index
                right_index = left_index + 1
            else:
                if profit > max_profit:
                    max_profit = profit
                right_index += 1
        return max_profit


```

