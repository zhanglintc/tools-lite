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
        this_lst = [None for i in range(len(num))]
        self.permute_helper(num, this_lst, fina_lst)
        return fina_lst

    def permute_helper(self, num, this_lst, fina_lst):
        length = len(num)
        if not num:
            fina_lst.append(this_lst[:])

        for i in range(length):
            this_lst[length - 1] = num[i] # set the last index
            self.permute_helper(num[:i] + num[i + 1:], this_lst, fina_lst)


