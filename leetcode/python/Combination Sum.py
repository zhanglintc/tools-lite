# Combination Sum
# for leetcode problems
# 2014.11.24 by zhanglin

# Problem:
# Given a set of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 2,3,6,7 and target 7,
# A solution set is:
# [7]
# [2, 2, 3]

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        fina_lst = []
        this_lst = []

        candidates.sort() # make it non-descending order
        self.combinationSum_helper(candidates, target, 0, this_lst, fina_lst)

        return fina_lst

    def combinationSum_helper(self, candidates, target, cur_sum, this_lst, fina_lst):
        for i in range(len(candidates)):
            # not enough to target, recursive
            if cur_sum + candidates[i] < target:
                this_lst.append(candidates[i])
                self.combinationSum_helper(candidates[i:], target, cur_sum + candidates[i], this_lst, fina_lst)
                this_lst.pop() # must pop() after append()

            # meet the target, append to fina_lst
            elif cur_sum + candidates[i] == target:
                this_lst.append(candidates[i])
                fina_lst.append(this_lst[:])
                this_lst.pop() # must pop() after append()
                return

            # overflow, just return
            else:
                return


