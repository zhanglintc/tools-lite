# Single Number
# for leetcode problems
# 2014.08.20 by zhanglin

# Problem:
# Given an array of integers, every element appears twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        times = {}
        for i in A:
            if i not in times:
                times[i] = 1
            else:
                times[i] += 1

        for key, val in times.items():
            if val == 1:
                return key


