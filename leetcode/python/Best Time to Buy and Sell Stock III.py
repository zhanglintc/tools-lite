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

        for i in range(len(prices)):
            left  = self.maxProfit_helper(prices[:i])
            right = self.maxProfit_helper(prices[i:])
            profit = max(profit, left + right)

        return profit

    def maxProfit_helper(self, prices):
        profit = 0 # the maximum profit

        if prices == []: # special case
            return profit

        lowest = prices[0] # from the very fisrt position 0, try to find the lowest price

        for i in range(1, len(prices)): # 1 to end
            lowest = min(lowest, prices[i]) # try to find the lowest
            profit = max(profit, prices[i] - lowest) # try to find the maximum profit

        return profit

