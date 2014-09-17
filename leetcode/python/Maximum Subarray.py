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

        mid_max = A[mid - 1]
        left = A[mid - 1]
        i = mid - 2
        while i >= 0:
            mid_max += A[i]
            left = max(mid_max, left)
            i -= 1

        mid_max = A[mid]
        right = A[mid]
        i = mid + 1
        while i < len(A):
            mid_max += A[i]
            right = max(mid_max, right)
            i += 1

        return max(left_max, left + right, right_max)


