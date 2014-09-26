# Unique Paths II
# for leetcode problems
# 2014.09.26 by zhanglin

# Problem:
# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

# Note: m and n will be at most 100.

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        # get the height and width
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # reverse every element in this Grid, after this, 0 means obstacle
        for row in range(m):
            for line in range(n):
                obstacleGrid[row][line] ^= 1

        # initial first row, if previous step is obstacle, set this step as obstacle, too
        for row in range(1, m):
            obstacleGrid[row][0] &= obstacleGrid[row - 1][0]

        # initial first line, if previous step is obstacle, set this step as obstacle, too
        for line in range(1, n):
            obstacleGrid[0][line] &= obstacleGrid[0][line - 1]

        # DP[row][line] = DP[row - 1][line] + DP[row][line - 1]
        for row in range(1, m):
            for line in range(1, n):
                if obstacleGrid[row][line]: # calculate if this step is NOT 0, otherwise do nothing
                    obstacleGrid[row][line] = obstacleGrid[row - 1][line] + obstacleGrid[row][line - 1]
                else: # obstacleGrid[row][line] == 0
                    pass

        return obstacleGrid[m - 1][n - 1] # the answer you need, :D


