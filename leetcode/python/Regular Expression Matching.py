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
        dp = [[False for cur_pat in range(len(p) + 1)] for cur_str in range(len(s) + 1)]

        dp[0][0] = True

        # check patterns can match first character or not
        for cur_pat in range(1, len(p) + 1):
            if p[cur_pat - 1] == '*':
                if cur_pat > 1:
                    dp[0][cur_pat] = dp[0][cur_pat - 2]

        # check the other characters
        for cur_str in range(1, len(s) + 1):
            for cur_pat in range(1, len(p) + 1):
                if p[cur_pat - 1] == '*':
                    dp[cur_str][cur_pat] = (dp[cur_str][cur_pat - 1] or dp[cur_str][cur_pat - 2]) or (dp[cur_str - 1][cur_pat] and (s[cur_str - 1] == p[cur_pat - 2] or p[cur_pat - 2] == '.'))

                else:
                    dp[cur_str][cur_pat] = dp[cur_str - 1][cur_pat - 1] and (s[cur_str - 1] == p[cur_pat - 1] or p[cur_pat - 1] == '.')

        return dp[len(s)][len(p)]


