// Best Time to Buy and Sell Stock III
// for leetcode problems
// 2014.09.12 by zhanglin

// Problem:
// Say you have an array for which the i[th] element is the price of a given stock on day i.

// Design an algorithm to find the maximum profit. You may complete at most TWO transactions.

// Note:
// You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution
{
public:
    int maxProfit_helper(vector<int> v)
    {
        int profit = 0;

        if(v.size() == 0)
        {
            return profit;
        }

        int lowest = v[0];

        for(int i = 0; i < v.size(); i++)
        {
            lowest = min(lowest, v[i]);
            profit = max(profit, v[i] - lowest);
        }

        return profit;
    }

    int maxProfit(vector<int> &prices)
    {
        vector<int> v;
        int profit = 0;
        int left;
        int right;

        for(int i = 0; i < prices.size(); i++)
        {
            v.assign(prices[0], prices[i]);
            left  = maxProfit_helper(v);
            v.assign(prices[i], prices[prices.size()]);
            right = maxProfit_helper(v); 
        }

        profit = max(profit, left + right);
    }
};


