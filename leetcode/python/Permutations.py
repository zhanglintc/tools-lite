# Permutations
# for leetcode problems
# 2014.09.23 by zhanglin

# Problem:
# Given a collection of numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

# See Combinations.py
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        fina_lst = []

        if len(num) == 1:
            return [num]

        for i in range(len(num)):
            for SortedList in self.permute(num[:i] + num[i + 1:]):
                fina_lst.append([num[i]] + SortedList) # fixnum + sortedlist

        return fina_lst
        

