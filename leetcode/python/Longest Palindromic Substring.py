# Longest Palindromic Substring
# for leetcode problems
# 2014.09.08 by zhanglin

# Problem:
# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000,
# and there exists one unique longest palindromic substring.

# What is Palindrome:
# Palindrome is a word, phrase, or sequence that reads the same backwards as forwards,
# e.g. madam or nurses run.

class Solution:
    # @return a string
    def Palindrome(self, s, i, j):
        while i > 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        len_max = (j - 1) - (i + 1) + 1

        return len_max

    def longestPalindrome(self, s):
        pass

