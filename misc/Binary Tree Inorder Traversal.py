# Binary Tree Inorder Traversal
# for leetcode problems
# 2014.09.15 by zhanglin

# Problem:
# Given a binary tree, return the inorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].

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
    def inorderTraversal(self, root):
        lst = []
        stack = []

        explorer = root
        while stack != [] or explorer != None:
            if explorer != None:
                stack.append(explorer)
                explorer = explorer.left

            else: # explorer == None
                explorer = stack.pop()
                lst.append(explorer.val)
                explorer = explorer.right

        return lst


