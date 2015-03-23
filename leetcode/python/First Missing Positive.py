# First Missing Positive
# for leetcode problems
# 2014.12.11 by zhanglin

# Problem:
# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space.

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if not A:
            return 1

        maxmum = max(A)

        for i in range(1, maxmum):
            if i not in A:
                return i

        return maxmum + 1


