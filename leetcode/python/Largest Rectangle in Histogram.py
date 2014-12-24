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
        if not height:
            return 0

        stk = []
        area = height[0]
        height.append(0)

        for i in range(len(height)):
            if not stk or height[stk[-1]] <= height[i]:
                stk.append(i)

            while height[stk[-1]] > height[i]:
                thisIdx = stk.pop()
                stk.append(i)
                thisArea = height[thisIdx] * (i if not stk else (i - thisIdx))
                area = thisArea if thisArea > area else area

        return area

s = Solution()
print s.largestRectangleArea([2,1,5,6,2,3])

