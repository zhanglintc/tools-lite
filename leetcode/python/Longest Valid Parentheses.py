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
        max = 0
        cur = 0

        for i in s:
            if stack == [] and i == ')':
                if max < cur:
                    max = cur 
                    cur = 0
                continue
            
            if i == '(':
                stack.append(i)
                cur += 1

            elif i == ')':
                stack.pop()
                cur += 1

        if max < cur:
            max = cur

        return max

