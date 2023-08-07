#You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        minimum: int = 10000
        profit: int = 0

        for i in range(len(prices)):
            minimum = min(prices[i], minimum)
            profit = max(profit, (prices[i]-minimum))

        return profit