# Reverse Words in a String
# for leetcode problems
# 2014.06.27 by zhanglin

# Problem:
# Given an input string, reverse the string word by word.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

# Update (2015-02-12):
# For C programmers: Try to solve it in-place in O(1) space.

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        lst = s.split()
        lst.reverse()
        str = " ".join(lst)
        return str


