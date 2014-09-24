# Permutations II
# for leetcode problems
# 2014.09.24 by zhanglin

# Problem:
# Given a collection of numbers that might contain duplicates,
# return all possible UNIQUE permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        fina_lst = []
        this_lst = [None for i in range(len(num))]
        self.permute_helper(num, this_lst, fina_lst)
        return fina_lst

    def permute_helper(self, num, this_lst, fina_lst):
        length = len(num)
        occurred = [] # store the used numbers
        if not num:
            fina_lst.append(this_lst[:])

        for i in range(length):
            if num[i] not in occurred: # if this number hasn't occured before, store it and process, otherwise do nothing
                occurred.append(num[i])
                this_lst[length - 1] = num[i] # set the last index
                self.permute_helper(num[:i] + num[i + 1:], this_lst, fina_lst)



