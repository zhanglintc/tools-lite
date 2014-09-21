# Container With Most Water
# for leetcode problems
# 2014.09.20 by zhanglin

# Problem:
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container.

class Solution:
    # @return an integer
    def maxArea(self, height):
        left  = height.pop(0)
        right = height.pop()

        capacity = min(left, right) * (len(height) + 1) # calculate the capacity

        while height: # while height not NULL, continue to try
            if left < right: # if left is shorter, use the one next to it
                left = height.pop(0)
            else: # if right is shorter, use the one next to it
                right = height.pop()

            capacity = max(capacity, min(left, right) * (len(height) + 1)) # recalculate the capacity

        return capacity


