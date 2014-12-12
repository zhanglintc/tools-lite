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
        fac = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

        for i in range(k - 1):
            sequence = self.nextPermutation(sequence)

        return ''.join(sequence)

    def factorial(self, n):
        fac = 1
        for i in range(n):
            fac *= (i + 1)

        return fac


