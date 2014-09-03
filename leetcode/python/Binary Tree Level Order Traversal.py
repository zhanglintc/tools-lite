# Binary Tree Level Order Traversal
# for leetcode problems
# 2014.09.02 by zhanglin

# Problem:
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        dikt = {}
        self.levelOrder_helper(root, 1, dikt)

        lst = []
        for i in dikt:
            lst.append(dikt[i])

        return lst

    def levelOrder_helper(self, root, dept, dikt):
        if root == None:
            return root

        if dept not in dikt:
            dikt[dept] = []
        
        dikt[dept].append(root.val)

        self.levelOrder_helper(root.left,  dept + 1, dikt)
        self.levelOrder_helper(root.right, dept + 1, dikt)

