# Binary Tree Zigzag Level Order Traversal
# for leetcode problems
# 2014.09.04 by zhanglin

# Problem:
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
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
    def zigzagLevelOrder(self, root):
        dikt = {}
        self.zigzagLevelOrder_helper(root, 1, dikt)

        lst = []
        for i in dikt:
            if i & 0x01 == 0: # if even line, reverse this line to make the traversal zigzag
                dikt[i].reverse()
            lst.append(dikt[i])

        return lst

    def zigzagLevelOrder_helper(self, root, dept, dikt):
        if root == None:
            return root

        if dept not in dikt:
            dikt[dept] = []
        
        dikt[dept].append(root.val)

        self.zigzagLevelOrder_helper(root.left,  dept + 1, dikt)
        self.zigzagLevelOrder_helper(root.right, dept + 1, dikt)

