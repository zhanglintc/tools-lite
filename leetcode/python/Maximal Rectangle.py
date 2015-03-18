# Maximal Rectangle
# for leetcode problems
# 2015.02.10 by zhanglin

# Problem:
# Given a 2D binary matrix filled with 0's and 1's,
# find the largest rectangle containing all ones and return its area.

# see Largest Rectangle in Histogram.py
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer

    # see Largest Rectangle in Histogram.py
    def largestRectangleArea(self, height):
        stk = [] # store every start of ascending chain
        area = 0 # result

        i = 0
        height.append(0) # append a 0 makes the code more elegant
        while i < len(height):
            if not stk or height[i] >= height[stk[-1]]: # ascending chain
                stk.append(i)
                i += 1

            else: # descending chain
                this = stk.pop() # use this height
                width = i if not stk else i - stk[-1] - 1 # but use the previous check point(don't forget 1 offset)
                area = max(area, width * height[this]) # upadate max area

        return area

    def transformMatrix(self, matrix):
        """
        Input:                  Middle:                  Output:
            matrix = [              matrix = [              matrix = [
                "111",                  [1,1,1],                  [1,1,1],
                "111",                  [1,1,1],                  [2,2,2],
                "101"]                  [1,0,1]]                  [3,0,3]]
        """
        # make string to list, and make string to int
        for row in range(len(matrix)):
            matrix[row] = list(matrix[row])

            for i in range(len(matrix[row])):
                matrix[row][i] = int(matrix[row][i])

        # transform matrix
        for row in range(len(matrix)-1, -1, -1):
            for line in range(len(matrix[row])):
                if matrix[row][line]:
                    fake_row = row - 1
                    while matrix[fake_row][line] and fake_row >= 0:
                        matrix[row][line] += 1
                        fake_row -= 1

    # main function
    def maximalRectangle(self, matrix):
        self.transformMatrix(matrix)

        area = 0
        for row in matrix:
            area = max(area, self.largestRectangleArea(row))

        return area


