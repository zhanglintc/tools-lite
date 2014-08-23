# Rotate Image
# for leetcode problems
# 2014.08.21 by zhanglin

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        length = len(matrix)
        if length <= 1:
            return matrix

        new_matrix = matrix
        for x in range(length):
            for y in range(length):
                new_matrix[y][length - 1 - x] = matrix[x][y]

        return new_matrix
