# Longest Valid Parentheses
# for leetcode problems
# 2014.09.05 by zhanglin

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        fin_max = 0
        cur_max = 0
        cur = 0

        for i in s: # traverse the whole input string
            if stack == [] and i == ')':
                if fin_max < cur:
                    fin_max = cur
                cur = 0
                continue
            
            if i == '(':
                stack.append(i)

            elif i == ')':
                stack.pop()
                cur += 1

        if fin_max < cur:
            fin_max = cur

        return fin_max * 2

