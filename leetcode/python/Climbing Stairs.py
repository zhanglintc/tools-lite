# Climbing Stairs
# for leetcode problems
# 2014.09.27 by zhanglin

# Problem:
# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 1:
            return 1

        if n == 2:
            return 2

        dp = [None for i in range(n)]

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n - 1]



