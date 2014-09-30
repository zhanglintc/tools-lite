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
        if len(matrix) == 0:
            return False

        if len(matrix) == 1:
            return (True if matrix[0] == target else False)

        mid = len(matrix) // 2
        if matrix[mid] == target:
            return True

        else:
            return (
                self.searchMatrix(matrix[:mid], target)
                if target < matrix[mid] else
                self.searchMatrix(matrix[mid+1:], target)
                )

s = Solution()
print s.searchMatrix([1,2,3,4,5,6.5], 6.5)


