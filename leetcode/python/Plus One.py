# Plus One
# for leetcode problems
# 2014.09.27 by zhanglin

# Problem:
# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        # the smallest digit process
        add_flag = 0
        digits[-1] += 1
        if digits[-1] >= 10:
            digits[-1] %= 10
            add_flag = 1

        # normal process
        for i in range(len(digits) - 2, -1, -1):
            digits[i] = (digits[i] + 1 if add_flag else digits[i])
            add_flag = 0

            if digits[i] >= 10:
                digits[i] %= 10
                add_flag = 1

        # the most significant digit process
        if add_flag:
            digits.insert(0, 1)

        return digits


