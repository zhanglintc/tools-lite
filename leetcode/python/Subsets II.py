# Subsets II
# for leetcode problems
# 2014.10.27 by zhanglin

# Problem:
# Given a collection of integers that might contain duplicates, S, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

# See Subsets.py
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        fina_lst = []
        this_lst = [None for i in range(len(S))]

        for req_depth in range(0, len(S) + 1):
            self.subsetsWithDup_helper(S, req_depth, 0, 0, fina_lst, this_lst)

        return fina_lst

    def subsetsWithDup_helper(self, S, req_depth, this_depth, start, fina_lst, this_lst):
        if this_depth == req_depth:
            if this_lst[:req_depth] not in fina_lst: # the only difference from Subsets.py
                fina_lst.append(this_lst[:req_depth])
            return

        for i in range(start, len(S)):
            this_lst[this_depth] = S[i]

            # break if can not reach the required depth
            if len(S) - i < req_depth - this_depth:
                break

            self.subsetsWithDup_helper(S, req_depth, this_depth + 1, i + 1, fina_lst, this_lst) # must be i + 1, not start + 1

s = Solution()
print s.subsetsWithDup([1,2,3])

