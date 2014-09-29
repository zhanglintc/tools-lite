# Spiral Matrix II
# for leetcode problems
# 2014.09.29 by zhanglin

# Problem:
# Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if not n:
            return []

        matrix = [[None for i in range(n)] for i in range(n)]

        spiralTraversal = range(1, n ** 2 + 1)
        direction = 0 # 0 for left->right, 1 for up->down, 2 for right->left, 3 for down->up

        row_start  = 0
        row_end    = len(matrix)
        line_start = 0
        line_end   = len(matrix[0])

        while True:
            if direction == 0:
                for i in range(line_start, line_end):
                    matrix[row_start][i] = spiralTraversal.pop(0)
                row_start += 1 # remove first row

            if direction == 1:
                for i in range(row_start, row_end):
                    matrix[i][line_end - 1] = spiralTraversal.pop(0)
                line_end -= 1 # remove last line

            if direction == 2:
                for i in range(line_end - 1, line_start - 1, -1): # -1 for offset
                    matrix[row_end - 1][i] = spiralTraversal.pop(0)
                row_end -= 1 # remove last row

            if direction == 3:
                for i in range(row_end - 1, row_start - 1, -1): # -1 for offset
                    matrix[i][line_start] = spiralTraversal.pop(0)
                line_start += 1 # remove first line

            if row_start == row_end or line_start == line_end: # use 'or' no matter row or line meets
                break # break if meets

            direction += 1 # change dirction
            direction %= 4 # reset if overflow

        return matrix


