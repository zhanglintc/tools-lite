# Jump Game II
# for leetcode problems
# 2014.12.07 by zhanglin

# Problem:
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.

# For example:
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2.
# (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        dp = [i for i in range(len(A))]

        for i in range(len(A)):
            for j in range(1, A[i] + 1):
                if i + j < len(A) and dp[i] + 1 < dp[i + j]:
                    dp[i + j] = dp[i] + 1

        return dp[-1]

s = Solution()
print s.jump([2,3,1,1,4])


