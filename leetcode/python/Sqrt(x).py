# Sqrt(x)
# for leetcode problems
# 2014.12.11 by zhanglin

# Problem:
# Implement int sqrt(int x).

# Compute and return the square root of x.

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        guess = 0x5f375a86

        while True:
            result = (guess + x / guess) / 2.0
            if abs(guess - result) < 0.000000000005:
                break

            guess = result

        return int(result)


