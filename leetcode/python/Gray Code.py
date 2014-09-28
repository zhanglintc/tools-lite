# Gray Code
# for leetcode problems
# 2014.09.28 by zhanglin

# Problem:
# The gray code is a binary numeral system where two successive values differ in only one bit.

# Given a non-negative integer n representing the total number of bits in the code,
# print the sequence of gray code. A gray code sequence must begin with 0.

# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# Note:
# For a given n, a gray code sequence is not uniquely defined.

# For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

# For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]

        if n == 1:
            return [0, 1]

        prev_codelist = self.grayCode(n - 1) # get the previous Gray Code list
        this_codelist = []

        # append the previous numbers to this_codelist
        for num in prev_codelist:
            this_codelist.append(num)

        # make prev_codelist mirrored and insert 1 to the very first position
        for num in prev_codelist[::-1]:
            fix = 1 << (n - 1)
            this_codelist.append(fix + num)

        return this_codelist


