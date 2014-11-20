# Jump Game
# for leetcode problems
# 2014.11.05 by zhanglin

# Problem:
# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return true.

# A = [3,2,1,0,4], return false.

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        available_step = A[0]

        for provided_step in A[1:]:
            available_step -= 1

            if available_step < 0:
                return False

            available_step = max(available_step, provided_step)

        return True


