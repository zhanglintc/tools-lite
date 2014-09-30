# Set Matrix Zeroes
# for leetcode problems
# 2014.09.30 by zhanglin

# Problem:
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        boolean_row  = [False for i in range(len(matrix))]
        boolean_line = [False for i in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for line in range(len(matrix[0])):
                if matrix[row][line] == 0:
                    boolean_row[row]   = True
                    boolean_line[line] = True

        for row in range(len(matrix)):
            for line in range(len(matrix[0])):
                if boolean_row[row] or boolean_line[line]:
                    matrix[row][line] = 0


