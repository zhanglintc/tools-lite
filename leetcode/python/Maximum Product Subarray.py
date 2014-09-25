# Maximum Product Subarray
# for leetcode problems
# 2014.09.24 by zhanglin

# Problem:
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        left  = 0
        right = 0
        fina_max = A[0]
        
        for i in A:
            if i != 0:
                if left == 0:
                    left = i
                else:
                    left = left * i
            else:
                left = 0

            fina_max = max(left, fina_max)
            
        for i in A[::-1]:
            if i != 0:
                if right == 0:
                    right = i
                else:
                    right = right * i
            else:
                right = 0

            fina_max = max(right, fina_max)

        return fina_max


