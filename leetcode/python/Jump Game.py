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
        bool_list = [False for i in range(len(A))]
        bool_list[-1] = True

        for i in range(len(A) - 2, -1, -1):
            for step in range(1, A[i] + 1):
                if bool_list[i + step] == True:
                    bool_list[i] = True
                    break

        if bool_list[0] == True:
            return True
        else:
            return False

s = Solution()
print s.canJump([1,2,0,1,4])


