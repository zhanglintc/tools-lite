# Remove Duplicates from Sorted Array II
# for leetcode problems
# 2014.10.20 by zhanglin

# Problem:
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array A = [1,1,1,2,2,3],

# Your function should return length = 5, and A is now [1,1,2,2,3].

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A == []:
            return 0

        new_idx = 0
        times = 1
        for i in range(1, len(A)):
            # if new digit occurred
            if A[new_idx] != A[i]:
                new_idx += 1
                A[new_idx] = A[i]

                times = 1

            # this digit occurred before
            else:
                # but less than twice
                if times < 2:
                    new_idx += 1
                    A[new_idx] = A[i]

                times += 1

        return new_idx + 1


