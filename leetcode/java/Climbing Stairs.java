// Climbing Stairs
// for leetcode problems
// 2015.02.04 by zhanglin

// Problem:
// You are climbing a stair case. It takes n steps to reach to the top.

// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

public class Solution {
    public int climbStairs(int n) {
        if(n == 1)
            return 1;

        if(n == 2)
            return 2;

        int[] dp = new int[n];

        dp[0] = 1;
        dp[1] = 2;

        for(int i = 2; i < n; i++) {
            dp[i] = dp[i - 2] + dp[i - 1];
        }

        return dp[n - 1];
    }
}


