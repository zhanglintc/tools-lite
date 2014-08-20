# Reverse Integer
# for leetcode problems
# 2014.08.20 by zhanglin

class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0:
            return x

        if x < 0:
            sign = -1
        else:
            sign = 1

        x = x * sign
        
        lst = []
        while x != 0:
            lst.append(x % 10)
            x //= 10

        while lst != []:
            x = x * 10 + lst.pop(0)

        return x * sign


input = 10100
S = Solution()
print(S.reverse(input))