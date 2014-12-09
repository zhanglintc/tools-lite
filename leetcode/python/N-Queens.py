# N-Queens
# for leetcode problems
# 2014.12.08 by zhanglin

# Problem:
# The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.

# Picture see: https://oj.leetcode.com/problems/n-queens/

# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.

# For example,
# There exist two distinct solutions to the 4-queens puzzle:

# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        # board's Nth value M represents
        # a Queen is put in M line in the N row
        board = [0 for i in range(n)]
        fina_lst = []

        # get all solutions
        self.dfs(0, n, board, fina_lst)

        # parse board to visible type
        for solution in fina_lst:
            for row in range(len(solution)):
                solution[row] = '.' * solution[row] + 'Q' + '.' * (n - 1 - solution[row])

        return fina_lst

    # check if target_row and target_line if valid or not
    def isValid(self, target_row, target_line, board):
        for row in range(target_row):
            if board[row] == target_line or abs(row - target_row) == abs(board[row] - target_line):
                return False

        return True

    # recursive
    def dfs(self, start_row, n, board, fina_lst):
        if start_row == n:
            fina_lst.append(board[:]) # don't forget "[:]" after board

        for row in range(start_row, n):
            for line in range(n):
                if self.isValid(row, line, board):
                    board[row] = line
                    self.dfs(row + 1, n, board, fina_lst)

                else: # not necessary
                    pass

            return # necessary

        return # not necessary


