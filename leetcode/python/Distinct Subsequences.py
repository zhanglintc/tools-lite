# Distinct Subsequences
# for leetcode problems
# 2014.12.05 by zhanglin

# Problem:
# Given a string S and a string T, count the number of distinct subsequences of T in S.

# A subsequence of a string is a new string which is formed from the original string bydeleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters.
# (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# Here is an example:
# S = "rabbbit", T = "rabbit"

# Return 3.

# Refer to: http://blog.csdn.net/abcbc/article/details/8978146
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        # dp length is dp[S + 1][T + 1]
        # thus there is offset between dp and S or T
        # dp[s][t] while S[s - 1], T[t - 1]
        dp = [[0 for t in range(len(T) + 1)] for s in range(len(S) + 1)]
        
        # initialize
        for s in range(len(S) + 1):
            dp[s][0] = 1

        # dynamic planning
        for s in range(1, len(S) + 1):
            for t in range(1, len(T) + 1):
                dp[s][t] = (dp[s - 1][t] + dp[s - 1][t - 1]) if (S[s - 1] == T[t - 1]) else (dp[s - 1][t])

        return dp[-1][-1]


