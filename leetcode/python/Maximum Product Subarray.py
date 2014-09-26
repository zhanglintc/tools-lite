# Maximum Product Subarray
# for leetcode problems
# 2014.09.24 by zhanglin

# Problem:
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

# O(2n) time
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        # initialize
        left  = 0
        right = 0
        fina_max = A[0]
        
        # from left to right
        for i in A: 
            left = (left * i if left != 0 else i)
            fina_max = max(left, fina_max)
        
        # from right to left
        for i in A[::-1]:
            right = (right * i if right != 0 else i)
            fina_max = max(right, fina_max)

        return fina_max


