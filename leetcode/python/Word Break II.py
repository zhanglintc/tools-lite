# Word Break II
# for leetcode problems
# 2015.02.04 by zhanglin

# Problem:
# Given a string s and a dictionary of words dict,
# add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        fina_lst = []
        if self.hasAnswer(s, dict):
            self.getAnswer(s, dict, "", fina_lst)

        return fina_lst

    def hasAnswer(self, s, dict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True

        return dp[-1]

    def getAnswer(self, s, dict, this_lst, fina_lst):
        if not s:
            fina_lst.append(this_lst[1:])

        for i in range(1, len(s) + 1):
            if s[:i] in dict:
                self.getAnswer(s[i:], dict, this_lst + " " + s[:i], fina_lst)


