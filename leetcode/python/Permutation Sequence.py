# Permutation Sequence
# for leetcode problems
# 2014.12.11 by zhanglin

# Problem:
# The set [1,2,3,...,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note: Given n will be between 1 and 9 inclusive.

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        sequence = ['1', '2', '3', '4', '5','6','7', '8', '9'][:n]

        for i in range(k - 1):
            sequence = self.nextPermutation(sequence)

        return ''.join(sequence)

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


