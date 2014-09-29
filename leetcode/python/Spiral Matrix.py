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
        self.spiralOrder_helper(matrix, spiralTraversal, 0, len(matrix), 0, len(matrix[0]))
        return spiralTraversal

    def spiralOrder_helper(self, matrix, spiralTraversal, row_start, row_end, line_start, line_end):
        if row_start == row_end - 1 and line_start == line_end - 1:
            spiralTraversal.append(matrix[row_start][line_start])
            return

        for i in range(line_start, line_end - 1): # left -> right
            spiralTraversal.append(matrix[0][i])

        for i in range(row_start, row_end - 1): # up -> down
            spiralTraversal.append(matrix[i][line_end - 1])

        for i in range(line_end - 1, line_start, -1): # right -> left
            spiralTraversal.append(matrix[row_end - 1][i])

        for i in range(row_end - 1, row_start, -1): # down -> up
            spiralTraversal.append(matrix[i][0])

        self.spiralOrder_helper(matrix, spiralTraversal, row_start + 1, row_end - 1, line_start + 1, line_end - 1)





lst = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
s = Solution()
print(s.spiralOrder(lst))


