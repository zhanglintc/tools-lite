# Min Stack
# for leetcode problems
# 2014.12.11 by zhanglin

# Problem:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, x):
        self.stack.append(x)

        if not self.minimum or x <= self.minimum[-1]:
            self.minimum.append(x)

    # @return nothing
    def pop(self):
        top = self.stack.pop()
        if top == self.minimum[-1]:
            self.minimum.pop()
        return top
        

    # @return an integer
    def top(self):
        return self.stack[-1]
        

    # @return an integer
    def getMin(self):
        return self.minimum[-1]


