# Edit Distance
# for leetcode problems
# 2014.12.04 by zhanglin

# Problem:
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
# (each operation is counted as 1 step.)

# You have the following 3 operations permitted on a word:

# a) Insert a character
# b) Delete a character
# c) Replace a character

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        dp = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]

        for i in range(1, len(word1) + 1):
            dp[i][0] = i

        for j in range(1, len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

        return dp[-1][-1]


