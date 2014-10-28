# Search for a Range
# for leetcode problems
# 2014.10.27 by zhanglin

# Problem:
# Given a sorted array of integers, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

# Time O(log n) Solution
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        start = 0
        end = len(A) - 1
        lst = [-1, -1]

        while start < end:
            mid = (start + end) // 2

            if A[mid] < target:
                start = mid + 1 # cause (start+end)//2 can become smaller, so here should be mid+1 to make ajust

            else:
                end = mid

        if A[start] != target:
            return lst
        else:
            lst[0] = start

        end = len(A)
        while start < end:
            mid = (start + end) // 2

            if A[mid] > target:
                end = mid

            else:
                start = mid + 1 # cause (start+end)//2 can become smaller, so here should be mid+1 to make ajust

        lst[1] = end - 1 # can I write Chinese here...

        return lst

