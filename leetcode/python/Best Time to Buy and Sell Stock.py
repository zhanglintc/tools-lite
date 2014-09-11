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
        profit = 0
        bought = False

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1] and bought == False:
                profit -= prices[i]
                bought = True

            if prices[i] > prices[i + 1] and bought == True:
                profit += prices[i]
                bought = False

        if bought == True:
            profit += prices[-1]

        return profit


