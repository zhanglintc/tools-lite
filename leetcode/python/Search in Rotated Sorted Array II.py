# Search in Rotated Sorted Array II
# for leetcode problems
# 2014.11.05 by zhanglin

# Problem:
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?

# Would this affect the run-time complexity? How and why?

# Write a function to determine if a given target is in the array.

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        for i in A:
            if i == target:
                return True
        return False


