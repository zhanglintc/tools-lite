# Factorial Trailing Zeroes
# for leetcode problems
# 2015.01.03 by zhanglin

# Problem:
# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        zeroes = 0

        while n:
            n /= 5
            zeroes += 1

        return zeroes


