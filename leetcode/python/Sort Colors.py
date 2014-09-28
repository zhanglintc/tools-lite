# Sort Colors
# for leetcode problems
# 2014.09.27 by zhanglin

# Problem:
# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note:
# You are not suppose to use the library's sort function for this problem.

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
# then 1's and followed by 2's.

# Could you come up with an one-pass algorithm using only constant space?

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        left  = 0 # index of red
        curr  = 0 # index of white
        right = len(A) - 1 # index of blue

        while curr != right + 1: # while curr doesn't meet right + 1
            # move left and curr
            if A[curr] == 0:
                A[left], A[curr] = A[curr], A[left]
                left += 1
                curr += 1

            # move right only(no need to move curr)
            elif A[curr] == 2:
                A[right], A[curr] = A[curr], A[right]
                right -= 1

            # move curr only(left and right stay the same position)
            else: # A[curr] == 1
                curr += 1


