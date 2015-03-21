# Sudoku Solver
# for leetcode problems
# 2015.03.20 by zhanglin

# Problem:
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# Empty cells are indicated by the character '.'.

# You may assume that there will be only one unique solution.

# Pictrue refer to: https://leetcode.com/problems/sudoku-solver/

# |5|3| | |7| | | | |
# |6| | |1|9|5| | | |
# | |9|8| | | | |6| |
# |8| | | |6| | | |3|
# |4| | |8| |3| | |1|
# |7| | | |2| | | |6|
# | |6| | | | |2|8| |
# | | | |4|1|9| | |5|
# | | | | |8| | |7|9|

# A sudoku puzzle...

# |5|3|4|6|7|8|9|1|2|
# |6|7|2|1|9|5|3|4|8|
# |1|9|8|3|4|2|5|6|7|
# |8|5|9|7|6|1|4|2|3|
# |4|2|6|8|5|3|7|9|1|
# |7|1|3|9|2|4|8|5|6|
# |9|6|1|5|3|7|2|8|4|
# |2|8|7|4|1|9|6|3|5|
# |3|4|5|2|8|6|1|7|9|

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
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

    def solveSudoku(self, board):
        pass


