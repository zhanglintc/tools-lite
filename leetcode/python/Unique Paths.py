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
        grid = [[None for i in range(n)] for i in range(m)] # make this map grid

        for row in range(m): # set all elements in first row as 1
            grid[row][0] = 1

        for line in range(n): # set all elements in first line as 1
            grid[0][line] = 1

        # DP[row][line] = DP[row - 1][line] + DP[row][line - 1]
        for row in range(1, m):
            for line in range(1, n):
                grid[row][line] = grid[row - 1][line] + grid[row][line - 1]

        return grid[m - 1][n - 1] # -1 for offset


