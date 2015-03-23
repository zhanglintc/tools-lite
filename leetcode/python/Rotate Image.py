# Rotate Image
# for leetcode problems
# 2014.08.21 by zhanglin

# Problem:
# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Follow up:
# Could you do this in-place?

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        length = len(matrix)
        if length <= 1:
            return matrix

        new_matrix = [[None] * length for i in range(length)] # new a matrix, here should be improved
        for x in range(length):
            for y in range(length):
                new_matrix[y][length - 1 - x] = matrix[x][y]

        return new_matrix


