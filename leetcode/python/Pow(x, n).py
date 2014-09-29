# Pow(x, n)
# for leetcode problems
# 2014.09.28 by zhanglin

# Problem:
# Implement pow(x, n).

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1

        elif n == 1:
            return x

        elif n == -1:
            return 1 / x
            
        elif n % 2 == 1:
            return self.pow(x * x, n // 2) * x

        elif n % 2 == 0:
            return self.pow(x * x, n // 2)

        else:
            pass


