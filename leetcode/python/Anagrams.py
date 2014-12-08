# Anagrams
# for leetcode problems
# 2014.12.08 by zhanglin

# Problem:
# Given an array of strings, return all groups of strings that are anagrams.

# Note: All inputs will be in lower-case.

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dikt = {}
        lst = []

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in dikt:
                dikt[sorted_word] = [word]
            else:
                dikt[sorted_word] = dikt[sorted_word] + [word]

        for i in dikt:
            if len(dikt[i]) >= 2:
                lst += dikt[i]

        return lst


