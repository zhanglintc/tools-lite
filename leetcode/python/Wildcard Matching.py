# Wildcard Matching
# for leetcode problems
# 2014.10.12 by zhanglin

# Problem:
# Implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "*") -> true
# isMatch("aa", "a*") -> true
# isMatch("ab", "?*") -> true
# isMatch("aab", "c*a*b") -> false

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        cur_str  = 0
        cur_patt = 0
        saved_str  = None
        saved_patt = None

        while cur_str < len(s):
            # matched (make sure cur_patt is not out of range)
            if cur_patt < len(p) and (p[cur_patt] == s[cur_str] or p[cur_patt] == '?'):
                cur_str  += 1
                cur_patt += 1

            # not matched
            else:
                # this is '*', save it (make sure cur_patt is not out of range)
                if cur_patt < len(p) and p[cur_patt] == '*':
                    saved_str  = cur_str
                    saved_patt = cur_patt
                    cur_patt += 1

                # this is not '*' (or cur_patt is out of range)
                # try to use the previous '*' position to match this one
                else:
                    # '*' has occurred before
                    if saved_patt != None:
                        saved_str += 1
                        cur_str  = saved_str
                        cur_patt = saved_patt + 1

                    # no '*' has occurred before
                    else:
                        return False

        # all characters in string has matched, chech the remaining in pattern
        while cur_patt < len(p):
            # if there is character which is not '*', then return False
            if p[cur_patt] != '*':
                return False

            cur_patt += 1

        # all is well, return True  :D
        return True


