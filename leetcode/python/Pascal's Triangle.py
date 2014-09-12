# Pascal's Triangle
# for leetcode problems
# 2014.09.12 by zhanglin

# Problem:
# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        triangle = []

        if numRows == 0:
            return triangle

        for row in range(numRows):
            if row == 0:
                triangle.append([1])

            else: # row[1] to row[n]
                pre_lst  = [0] + triangle[row - 1] + [0]
                this_lst = []

                for i in range(len(pre_lst) - 1):
                    this_lst.append(pre_lst[i] + pre_lst[i + 1])

                triangle.append(this_lst)

        return triangle

