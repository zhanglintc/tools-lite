# Regular Expression Matching
# for leetcode problems
# 2014.10.01 by zhanglin

# Problem:
# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "a*") -> true
# isMatch("aa", ".*") -> true
# isMatch("ab", ".*") -> true
# isMatch("aab", "c*a*b") -> true

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        # dp[string][pattern]
        #  i for string, j for pattern
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]

        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                if j > 1:
                    dp[0][j]=dp[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = (dp[i][j - 1] or dp[i][j - 2]) or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.')

                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')

        return dp[len(s)][len(p)]





s = Solution()
print (s.isMatch('aab','c*a*b'))

