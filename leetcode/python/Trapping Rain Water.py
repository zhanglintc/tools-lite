# Trapping Rain Water
# for leetcode problems
# 2014.10.27 by zhanglin

# Problem:
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.

# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

# 3|              _
# 2|      _      | |_   _
# 1|  _  | |_   _|   |_| |_
# 0| | | |   | |           |
#  |-------------------------
#   0 1 0 2 1 0 1 3 2 1 2 1 0

# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water are being trapped.
# Thanks Lane for contributing this image!

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if A == []:
            return 0

        water = 0 # the water can be trapped
        max_idx = A.index(max(A)) # index of highest plank

        sub_max = 0
        for i in range(max_idx): # from left to highest
            if A[i] < sub_max 
                water += sub_max - A[i]
            else:
                sub_max = A[i]

        sub_max = 0
        for i in range(len(A) - 1, max_idx, -1): # from right to highest
            if A[i] < sub_max 
                water += sub_max - A[i]
            else:
                sub_max = A[i]

        return water


