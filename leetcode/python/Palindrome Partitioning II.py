# Palindrome Partitioning II
# for leetcode problems
# 2014.12.03 by zhanglin

# Problem:
# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

# Hard to understand...
# Refer to http://blog.csdn.net/doc_sgl/article/details/13418125
# Refer to http://www.cnblogs.com/zuoyuan/p/3758783.html
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # dp for "dynamic plan", vp for "valid palindrome"
        dp = [0 for i in range(len(s) + 1)] # dp is one step longer than len(s), think about if whole string is a palindrome
        vp = [[False for j in range(len(s))] for i in range(len(s))]

        for i in range(len(s) + 1): # dp is one step longer than len(s), think about if whole string is a palindrome
            dp[i] = len(s) - i # least palindrome strings from position i to the end

        for i in range(len(s), -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 1 or vp[i + 1][j - 1]): # if pos i to pos j is palindrome
                    vp[i][j] = True
                    dp[i] = min(dp[i], dp[j + 1] + 1) # if i to j is palindrome, then dp[i] equals dp[j + 1] + 1, update dp[j]

        return dp[0] - 1 # cuts is one less than palindromes


