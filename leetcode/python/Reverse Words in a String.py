# Reverse Words in a String
# for leetcode problems
# 2014.06.27 by zhanglin

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        lst = s.split()
        lst.reverse()
        str = " ".join(lst)
        return str
