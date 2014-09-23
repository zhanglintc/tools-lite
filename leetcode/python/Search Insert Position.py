# Search Insert Position
# for leetcode problems
# 2014.09.23 by zhanglin

# Problem:
# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        for i in range(len(A)):
            if target <= A[i]: # equal means return this position, less means insert here
                return i

        return i + 1 # otherwise return the length + 1, means append at the end


