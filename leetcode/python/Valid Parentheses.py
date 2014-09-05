# Valid Parentheses
# for leetcode problems
# 2014.09.05 by zhanglin

# Problem:
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        left  = "({["
        right = ")}]"

        for item in s:
            if item in right and stack == []: # ")}]" occur but stack is None
                return False

            if item in left: # if "({[", push item to stack
                stack.append(item)

            elif item in right: # if ")}]"
                if stack[-1] == left[right.index(item)]: # if match last item in stack
                    stack.pop() # pop one item in stack and continue
                else: # else return false
                    return False

        # after traversal
        if stack == []:
            return True

        else:
            return False


