# Unique Paths
# for leetcode problems
# 2014.09.25 by zhanglin

# Problem:
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


# Above is a 3 x 7 grid. How many possible unique paths are there?

# Note: m and n will be at most 100.

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        return self.getRow(m, n)

    def getRow(self, m, n):
        cache   = [1]
        current = [1]

        for row in range(m + n - 2):
            cache  = [0] + cache + [0]
            current = []

            for i in range(len(cache) - 1):
                current.append(cache[i] + cache[i + 1])

            cache = current

        return current[min(m, n) - 1]


