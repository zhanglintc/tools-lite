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

        return len_max

    def longestPalindrome(self, s):
        odd  = 0
        even = 0
        fin_max = 0
        cur_max = 0

        for i in range(len(s)):
            odd = max(odd, self.Palindrome(s, i, i))
            if i < len(s) - 1:
                even = max(even, self.Palindrome(s, i, i + 1))

            cur_max = max(odd, even)
            if cur_max > fin_max:
                fin_max = cur_max
                if fin_max & 0x01:
                    start = i - (fin_max // 2)
                else:
                    start = i - (fin_max // 2 - 1)

        return s[start : start + fin_max]

