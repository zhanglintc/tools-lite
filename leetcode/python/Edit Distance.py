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

# Refer to http://www.cnblogs.com/zuoyuan/p/3773134.html
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        # word1: 0 -> i, word2: 0 -> j
        # dp:    0 -> i + 1     0 -> j + 1
        dp = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]

        # initialize
        for i in range(1, len(word1) + 1):
            dp[i][0] = i

        for j in range(1, len(word2) + 1):
            dp[0][j] = j

        # dynamic planning
        # using dp's index, and word's index is dp's index - 1
        # thus why dp[i][j] vs word[i - 1] word[j - 1], it's the same position
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                # if this two characters match
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                # if not match, then choose a method which has least convert steps
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

        return dp[-1][-1]


