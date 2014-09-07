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
        stack = [-1] # a stack which stores the index of the last unmatched '('
        fin_max = 0 # the answer
        
        for i in range(len(s)): # traverse the in put string
            if s[i] == '(': # if '(', update the stack
                stack.append(i)

            else: # else if ')'
                if len(stack) > 1: # if stack is not 'NULL', update the ans
                    stack.pop()
                    fin_max = max(fin_max, i - stack[-1])

                else: # if stack is 'NULL', update the last index
                    stack.pop()
                    stack.append(i)

        return fin_max

