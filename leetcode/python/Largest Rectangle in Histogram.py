# Largest Rectangle in Histogram
# for leetcode problems
# 2014.12.23 by zhanglin

# Problem:
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.

# 7|        _
# 6|      _| |
# 5|     |   |
# 4|     |   |  _
# 3|  _  |   |_| |
# 2| | |_|       |
# 1| |           |
# 0|-----------------
#   0 2 1 5 6 2 3

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

# 7|        _
# 6|      _| |
# 5|     |///|
# 4|     |///|  _
# 3|  _  |///|_| |
# 2| | |_|///    |
# 1| |    ///    |
# 0|-----------------
#   0 2 1 5 6 2 3

# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# For example,
# Given height = [2,1,5,6,2,3],
# return 10.

class Solution:
    # @param height, a list of integer
    # @return an integer
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


