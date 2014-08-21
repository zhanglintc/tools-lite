# Evaluate Reverse Polish Notation
# for leetcode problems
# 2014.07.07 by zhanglin

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        operators = "+-*/"
        stack = []
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if i is "+":
                    result = n1 + n2
                elif i is "-":
                    result = n1 - n2
                elif i is "*":
                    result = n1 * n2
                elif i is "/":
                    result = int(float(n1) / float(n2))
                stack.append(result)
        return stack.pop()
