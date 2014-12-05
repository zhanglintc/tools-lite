# Next Permutation
# for leetcode problems
# 2014.12.04 by zhanglin

# Problem:
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        for i in range(len(num) - 2, -1, -1):
            # find a number smaller than successor, called partition
            if num[i] < num[i + 1]:
                for j in range(len(num) - 1, i, -1):
                    # find first number greater than partition
                    if num[i] < num[j]:
                        num[i], num[j] = num[j], num[i] # swap
                        re = num[i + 1:] # and reverse numbers behind partition
                        re.reverse()
                        return num[:i + 1] + re

                    else: # Newton's third law. You gotta leave something behind! (behind if)
                        pass

            else: # Newton's third law. You gotta leave something behind! (behind if)
                pass

        num.reverse()
        return num


