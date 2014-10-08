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
        i, j = 0, 0
        length = min(len(s), len(p))
        dp = [False for i in range(length)]
        while i < length - 1 and j < length - 1:
            dp[i] = (s[i] == p[j] or p[j] == '.')
            i += 1
            j += 1

        return dp[i - 1] and (s[i] == p[j] or p[j] == '.')

s = Solution()
print (s.isMatch('aca','aca'))

