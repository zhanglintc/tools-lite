# Best Time to Buy and Sell Stock
# for leetcode problems
# 2014.09.11 by zhanglin

# Problem:
# Say you have an array for which the i[th] element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock)
# design an algorithm to find the maximum profit.

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0 # the maximum profit

        if prices == []: # special case
            return profit

        lowest = prices[0] # from the very fisrt position 0, try to find the lowest price

        for i in range(1, len(prices)): # 1 to end
            lowest = min(lowest, prices[i]) # try to find the lowest
            profit = max(profit, prices[i] - lowest) # try to find the maximum profit

        return profit



