# Add Two Numbers
# for leetcode problems
# 2014.09.29 by zhanglin

# Problem:
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if not matrix:
            return matrix

        spiralTraversal = []
        direction = 0 # 0 for left->right, 1 for up->down, 2 for right->left, 3 for down->up

        row_start  = 0
        row_end    = len(matrix)
        line_start = 0
        line_end   = len(matrix[0])

        while True:
            if direction == 0:
                for i in range(line_start, line_end):
                    spiralTraversal.append(matrix[row_start][i])
                row_start += 1 # remove first row

            if direction == 1:
                for i in range(row_start, row_end):
                    spiralTraversal.append(matrix[i][line_end - 1])
                line_end -= 1 # remove last line

            if direction == 2:
                for i in range(line_end - 1, line_start - 1, -1): # -1 for offset
                    spiralTraversal.append(matrix[row_end - 1][i])
                row_end -= 1 # remove last row

            if direction == 3:
                for i in range(row_end - 1, row_start - 1, -1): # -1 for offset
                    spiralTraversal.append(matrix[i][line_start])
                line_start += 1 # remove first line

            if row_start == row_end or line_start == line_end: # use 'or' no matter row or line meets
                break # break if meets

            direction += 1 # change dirction
            direction %= 4 # reset if overflow

        return spiralTraversal


