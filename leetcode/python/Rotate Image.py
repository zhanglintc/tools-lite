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
        for i in range(length):
            for j in range(length):
                new_matrix[j][length - 1 - i] = matrix[i][j]

        return new_matrix
