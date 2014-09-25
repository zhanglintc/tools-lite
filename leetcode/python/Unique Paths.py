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
        if min(m, n) == 1:
            return 1

        if m <= n:
            return n * self.uniquePaths(m - 1, n - 1)
        else:
            return m * self.uniquePaths(m - 1, n - 1)

s = Solution()
print s.uniquePaths(3,3)


