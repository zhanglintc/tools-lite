# Remove Duplicates from Sorted Array
# for leetcode problems
# 2014.09.15 by zhanglin

# Problem:
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array A = [1,1,2],

# Your function should return length = 2, and A is now [1,2].

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A == []:
            return 0

        new_idx = 0
        for i in range(1, len(A)):
            if A[new_idx] != A[i]:
                new_idx += 1
                A[new_idx] = A[i]

        return new_idx + 1


