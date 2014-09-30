# Search a 2D Matrix
# for leetcode problems
# 2014.09.30 by zhanglin

# Problem:
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False


        if len(matrix) == 1: # search in a single row
            if len(matrix[0]) == 1: # judge when only one element left
                return (True if matrix[0][0] == target else False)

            mid_idx = len(matrix[0]) // 2
            if target < matrix[0][mid_idx]: # search left
                return self.searchMatrix([ matrix[0][:mid_idx] ], target)
            else: # search right
                return self.searchMatrix([ matrix[0][mid_idx:] ], target)

        else: # if not single row, make it smaller
            mid_row = len(matrix) // 2
            if target < matrix[mid_row][0]: # search up
                return self.searchMatrix(matrix[:mid_row], target)
            else: # search down
                return self.searchMatrix(matrix[mid_row:], target)



