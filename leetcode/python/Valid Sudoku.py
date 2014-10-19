# Valid Sudoku
# for leetcode problems
# 2014.10.19 by zhanglin

# Problem:

# Refer to:
# https://oj.leetcode.com/problems/valid-sudoku/

# Determine if a Sudoku is valid.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

# A partially filled sudoku which is valid.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # check row
        for row in range(9):
            occurred = []
            for column in range(9):
                if board[row][column] not in occurred or board[row][column] == '.':
                    occurred.append(board[row][column])

                else:
                    return False

        # check column
        for column in range(9):
            occurred = []
            for row in range(9):
                if board[row][column] not in occurred or board[row][column] == '.':
                    occurred.append(board[row][column])

                else:
                    return False

        # check sub-box
        for base_row in range(3):
            for base_column in range(3):
                occurred = []
                for sub_row in range(3):
                    for sub_column in range(3):
                        real_row    = base_row * 3 + sub_row
                        real_column = base_column * 3 + sub_column
                        if board[real_row][real_column] not in occurred or board[real_row][real_column] == '.':
                            occurred.append(board[real_row][real_column])

                        else:
                            return False

        # all well, return True
        return True

