# Binary Tree Level Order Traversal II
# for leetcode problems
# 2014.09.04 by zhanglin

# Problem:
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
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
    def levelOrderBottom(self, root):
        dikt = {}
        self.levelOrderBottom_helper(root, 1, dikt)

        lst = []
        for i in dikt:
            lst.append(dikt[i])

        return lst[::-1] # the only different from "Binary Tree Level Order Traversal"

    def levelOrderBottom_helper(self, root, dept, dikt):
        if root == None:
            return root

        if dept not in dikt:
            dikt[dept] = []
        
        dikt[dept].append(root.val)

        self.levelOrderBottom_helper(root.left,  dept + 1, dikt)
        self.levelOrderBottom_helper(root.right, dept + 1, dikt)

