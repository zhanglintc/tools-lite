# Palindrome Number
# for leetcode problems
# 2014.09.20 by zhanglin

# Problem:
# Determine whether an integer is a palindrome. Do this without extra space.

# Some hints:
# Could negative integers be palindromes? (ie, -1)

# If you are thinking of converting the integer to string, note the restriction of using extra space.

# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

# There is a more generic way of solving this problem.

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0: # negative integer is not palindrome
            return False

        if x == self.reverse(x):
            return True

        else:
            return False

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


