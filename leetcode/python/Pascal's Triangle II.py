# Pascal's Triangle II
# for leetcode problems
# 2014.09.13 by zhanglin

# Problem:
# Given an index k, return the k[th] row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        cache   = [1]
        current = [1]

        for row in range(rowIndex):
            cache  = [0] + cache + [0]
            current = []

            for i in range(len(cache) - 1):
                current.append(cache[i] + cache[i + 1])

            cache = current

        return current


