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
        #           pattern pattern pattern
        # string
        # string
        # string
        dp = [[False for pattern in range(len(p) + 1)] for string in range(len(s) + 1)]

        dp[0][0] = True
        for string in range(1, len(s) + 1):
            for pattern in range(1, len(p) + 1):
                if p[pattern - 1] == '*':
                    dp[string][pattern] = dp[string][pattern - 1] or dp[string][pattern - 2] or dp[string - 1][pattern] # or dp[string - 1][pattern], why?!

                else:
                    dp[string][pattern] = dp[string - 1][pattern - 1] and (s[string - 1] == p[pattern - 1] or p[pattern - 1] == '.')

        return dp[len(s)][len(p)]





s = Solution()
print (s.isMatch('aca','.*.'))

