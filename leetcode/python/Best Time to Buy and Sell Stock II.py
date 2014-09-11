# Best Time to Buy and Sell Stock II
# for leetcode problems
# 2014.09.11 by zhanglin

# Problem:
# Say you have an array for which the i[th] element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times). 
# However, you may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0 # the maximum profit
        bought = False # you don't have stock in hand

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1] and bought == False: # low price and you don't have stock
                profit -= prices[i] # spend
                bought = True # set status to bought

            if prices[i] > prices[i + 1] and bought == True: # high price and you have stock
                profit += prices[i] # gain
                bought = False # set status to sold

        if bought == True: # if you have stock at the end, sell it
            profit += prices[-1] # gain (the last day's price)

        return profit # return your last profit



