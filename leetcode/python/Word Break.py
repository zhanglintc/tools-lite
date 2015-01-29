# Word Break
# for leetcode problems
# 2015.01.12 by zhanglin

# Problem:
# Given a string s and a dictionary of words dict,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not s and dict:
            return True

        word = ""
        for i in range(len(s)):
            word += s[i]
            if word in dict:
                return self.wordBreak(s[i + 1:], dict)

        return False

s = "aaaaaaa"
dict = ["aaaa", "aaa"]

ss = Solution()
print ss.wordBreak(s, dict)


