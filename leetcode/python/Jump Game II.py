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
        steps = 0 # steps to reach the end
        from_prev_step = 0 # longest position from previous check point
        can_be_reached = 0 # longest position can be reached from the very start

        for i in range(len(A)):
            if i > from_prev_step: # if you want to go further, you should take 'steps + 1' steps
                from_prev_step = can_be_reached
                steps += 1

            can_be_reached = max(can_be_reached, i + A[i])

        return steps


