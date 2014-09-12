# Best Time to Buy and Sell Stock III
# for leetcode problems
# 2014.09.12 by zhanglin

# Problem:
# Say you have an array for which the i[th] element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most TWO transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0

        if prices == []:
            return profit

        n = len(prices)

        left  = [0 for i in range(n)] # to store left  maximum profit, traverse from left to right
        right = [0 for i in range(n)] # to sotre right maximum profit, traverse from right to left

        lowest = prices[0]
        for i in range(1, n): # 1 to n -1, counting, O(n) time to find maximum profit for left slice
            lowest = min(lowest, prices[i])
            left[i] = max(prices[i] - lowest, left[i - 1])

        highest = prices[-1]
        for i in range(n - 2, -1, -1): # n - 1 to 1, reverse counting, O(n) time to find maximum profit for rifht slice
            highest = max(highest, prices[i])
            right[i] = max(highest - prices[i], right[i + 1])

        for i in range(len(prices)): # O(n) time to find maximum profit between each node's profit
            profit = max(profit, left[i] + right[i])

        return profit # O(3n) solution


