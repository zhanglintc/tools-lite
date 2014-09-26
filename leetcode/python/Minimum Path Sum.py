# Minimum Path Sum
# for leetcode problems
# 2014.09.26 by zhanglin

# Problem:
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# See Triangle.py and Unique Paths II.py
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        # get rows and lines
        m = len(grid)
        n = len(grid[0])

        # initial first row
        for row in range(1, m):
            grid[row][0] += grid[row - 1][0]

        # initial first line
        for line in range(1, n):
            grid[0][line] += grid[0][line - 1]

        # only store the minimum path sum every step
        for row in range(1, m):
            for line in range(1, n):
                grid[row][line] += min(grid[row - 1][line], grid[row][line - 1])

        return grid[m - 1][n - 1] # :D


