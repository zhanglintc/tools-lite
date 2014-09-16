# Combinations
# for leetcode problems
# 2014.09.16 by zhanglin

# Problem:
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:

# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        fina_lst = []                                       # final list, no need to initialize, we can use append method
        this_lst = [None for i in range(k)]                 # must be initialized, cause we should call it by index
        self.combine_helper(n, k, fina_lst, this_lst, 0, 1) # call main function
        return fina_lst

    def combine_helper(self, n, k, fina_lst, this_lst, depth, start):
        if depth == k:                                      # if reach k
            fina_lst.append(this_lst[:])                    # add the COPY of this_lst to fina_lst
            return

        else:                                               # not reach k
            for i in range(start, n + 1):                   # index is 0 ~ n while number is 1 ~ n + 1
                this_lst[depth] = i                         # set number to this depth
                self.combine_helper(n, k, fina_lst, this_lst, depth + 1, i + 1)

s = Solution()
print s.combine(10, 5)
