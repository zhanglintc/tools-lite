# Path Sum II
# for leetcode problems
# 2014.08.24 by zhanglin

# Problem:
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pahtSum_helper(self, root, sum, thisSum, thisList, mainList):
        thisList.append(root.val)

        if root.left == None and root.right == None:
            if sum == root.val + thisSum:
                mainList.append(thisList[:])

        if root.left != None:
            self.pahtSum_helper(root.left, sum, thisSum + root.val, thisList, mainList)
            thisList.pop()

        if root.right != None:
            self.pahtSum_helper(root.right, sum, thisSum + root.val, thisList, mainList)
            thisList.pop()

    def pathSum(self, root, sum):
        thisList = []
        mainList = []
        if root != None:
            self.pahtSum_helper(root, sum, 0, thisList, mainList)

        return mainList


