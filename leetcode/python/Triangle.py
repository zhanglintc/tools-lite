# Triangle
# for leetcode problems
# 2014.09.13 by zhanglin

# Problem:
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) <= 1: # special case
            return triangle[0][0]

        prev_sum_list = triangle[-1] # set prev list as the last row of triangle
        for row in range(len(triangle) - 2, -1, -1): # reverse count from triangle[-2] to triangle[0]

            this_sum_list = triangle[row]
            for i in range(len(this_sum_list)):
                this_sum_list[i] += min(prev_sum_list[i], prev_sum_list[i + 1]) # caculate the minimum path sum

            prev_sum_list = this_sum_list # store the last calculated results

        return this_sum_list[0] # after the for loop, there would be only one item in this_sum_list, return it


