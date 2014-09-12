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
        profits = []
        bought = False

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1] and bought == False:
                buy = prices[i]
                bought = True

            if prices[i] > prices[i + 1] and bought == True:
                sell = prices[i]
                bought = False
                profits.append(sell - buy)

        if bought == True:
            sell = prices[-1]
            profits.append(sell - buy)

        profits.sort()
        
        length = len(profits)
        if length == 0:
            profit = 0
        elif length == 1:
            profit = profits[-1]
        else:
            profit = profits[-2] + profits[-1]
        print(profits)
        return profit

s = Solution()
print (s.maxProfit([1,2,4,2,5,7,2,4,9,0]))

