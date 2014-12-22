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
        numberlist = ['1', '2', '3', '4', '5','6','7', '8', '9']
        sequence = ''

        k -= 1 # don't know why...
        while n:
            facto = self.factorial(n - 1) # (n - 1)th factorial
            this = numberlist[k / facto] # number to be added to final sequence

            sequence += this # add this number
            numberlist.remove(this) # remove it
            k %= facto # remaining k
            n -= 1 # n - 1 numbers remaining

        return sequence

    def factorial(self, n):
        facto = 1

        for i in range(n):
            facto *= (i + 1)

        return facto


