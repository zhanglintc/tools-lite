# Combination Sum II
# for leetcode problems
# 2014.11.25 by zhanglin

# Problem:
# Given a collection of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 10,1,2,7,6,1,5 and target 8,
# A solution set is:
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        fina_lst = []
        this_lst = []

        candidates.sort() # make it non-descending order
        self.combinationSum2_helper(candidates, target, 0, this_lst, fina_lst)

        return fina_lst

    def combinationSum2_helper(self, candidates, target, cur_sum, this_lst, fina_lst):
        for i in range(len(candidates)):
            # not enough to target, recursive
            if cur_sum + candidates[i] < target:
                this_lst.append(candidates[i])
                self.combinationSum2_helper(candidates[i + 1:], target, cur_sum + candidates[i], this_lst, fina_lst)
                this_lst.pop() # must pop() after append()

            # meet the target, append to fina_lst
            elif cur_sum + candidates[i] == target:
                this_lst.append(candidates[i])
                if this_lst not in fina_lst:
                    fina_lst.append(this_lst[:])
                this_lst.pop() # must pop() after append()
                return

            # overflow, just return
            else:
                return

s = Solution()
print s.combinationSum2([10,1,2,7,6,1,5], 8)
