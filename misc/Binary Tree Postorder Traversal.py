# Binary Tree Postorder Traversal
# for leetcode problems
# 2014.09.15 by zhanglin

# Problem:
# Given a binary tree, return the postorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Non-recursive solution
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        lst = []
        stack = []
        hasVisitied = None

        explorer = root
        while stack != [] or explorer != None:
            while explorer != None:
                stack.append(explorer)
                explorer = explorer.left

            explorer = stack[-1]
            if explorer.right == None or explorer.right == hasVisitied:
                lst.append(explorer.val)
                stack.pop()
                hasVisitied = explorer
                explorer = None

            else:
                explorer = explorer.right

        return lst



