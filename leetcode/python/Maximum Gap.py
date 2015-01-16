# Maximum Gap
# for leetcode problems
# 2015.01.04 by zhanglin

# Problem:
# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

# Try to solve it in linear time/space.

# Return 0 if the array contains less than 2 elements.

# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

# Credits:
# Special thanks to @porker2008 for adding this problem and creating all test cases.

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        gap = 0

        num.sort()

        for i in range(len(num) - 1):
            gap = max(gap, num[i + 1] - num[i])

        return gap


