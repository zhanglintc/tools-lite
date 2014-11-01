# Find Minimum in Rotated Sorted Array
# for leetcode problems
# 2014.10.31 by zhanglin

# Problem:
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# You may assume no duplicate exists in the array.

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num) == 0:
            return None
        elif len(num) == 1:
            return num[0]

        minimum = num[0]
        for i in range(1, len(num)):
            if num[i] < minimum:
                return num[i]

        return minimum


