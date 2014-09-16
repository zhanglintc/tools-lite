# Maximum Subarray
# for leetcode problems
# 2014.09.16 by zhanglin

# Problem:
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.

# More practice:
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        this_sum = A[0]
        max_sum  = A[0]
        for i in range(1, len(A)):
            this_sum = (A[i] if this_sum < 0 else this_sum + A[i])
            max_sum  = (this_sum if this_sum > max_sum else max_sum)

        return max_sum


