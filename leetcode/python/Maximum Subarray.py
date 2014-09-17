# Maximum Subarray
# for leetcode problems
# 2014.09.16 by zhanglin

# Problem:
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# More practice:
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 0:
            return None

        if len(A) == 1:
            return A[0]

        mid = len(A) // 2
        left_max  = self.maxSubArray(A[:mid])
        right_max = self.maxSubArray(A[mid:])

        mid_max = A[mid]
        temp = mid_max
        i = mid - 1
        while i >= 0:
            temp += A[i]
            mid_max = max(mid_max, temp)
            i -= 1

        temp = mid_max
        i = mid + 1
        while i < len(A):
            temp += A[i]
            mid_max = max(mid_max, temp)
            i += 1

        return max(left_max, mid_max, right_max)


