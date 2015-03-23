# Generate Parentheses
# for leetcode problems
# 2014.07.20 by zhanglin

# Problem:
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# "((()))", "(()())", "(())()", "()(())", "()()()"

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        ret = []
        if n == 0:
            return []
        self.helper(n, n, '', ret)
        return ret

    def helper(self, left, right, tmp, ret):
        if left == 0 and right == 0:
            ret.append(tmp)
        if left > 0:
            self.helper(left - 1, right, tmp + '(', ret)
        if right > 0 and left < right:
            self.helper(left, right - 1, tmp + ')', ret)


