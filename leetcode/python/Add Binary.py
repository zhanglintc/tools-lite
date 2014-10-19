# Add Binary
# for leetcode problems
# 2014.10.19 by zhanglin

# Problem:
# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        s = ''
        add_flag = 0

        a = list(a)
        b = list(b)
        while a and b:
            this = (int(a.pop()) + int(b.pop()) + add_flag if add_flag else int(a.pop()) + int(b.pop()))

            if this >= 2:
                add_flag = 1
                this %= 2

            else:
                add_flag = 0

            s = str(this) + s

        while a:
            this = (int(a.pop()) + add_flag if add_flag else int(a.pop()))

            if this >= 2:
                add_flag = 1
                this %= 2

            else:
                add_flag = 0

            s = str(this) + s

        while b:
            this = (int(b.pop()) + add_flag if add_flag else int(b.pop()))

            if this >= 2:
                add_flag = 1
                this %= 2

            else:
                add_flag = 0

            s = str(this) + s

        if add_flag:
            s = str(add_flag) + s

        return s


