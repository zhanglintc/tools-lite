# N-Queens II
# for leetcode problems
# 2014.12.09 by zhanglin

# Problem:
# Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.

# Picture see: https://oj.leetcode.com/problems/n-queens-ii/

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        # board's Nth value M represents
        # a Queen is put in M line in the N row
        board = [0 for i in range(n)]
        fina_lst = []

        # get all solutions
        self.dfs(0, n, board, fina_lst)

        return len(fina_lst)

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


