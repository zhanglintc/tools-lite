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
    def Palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        len_max = (r - 1) - (l + 1) + 1

        return len_max, l + 1

    def longestPalindrome(self, s):
        fina_max   = 0
        fina_start = 0

        for i in range(len(s)):
            odd_max,   odd_start = self.Palindrome(s, i, i)     # max length is odd
            even_max, even_start = self.Palindrome(s, i, i + 1) # max length is even

            if max(odd_max, even_max) > fina_max: # need update
                fina_max = max(odd_max, even_max)
                fina_start = (odd_start if odd_max > even_max else even_start) # set start position
        return s[fina_start : fina_start + fina_max]



