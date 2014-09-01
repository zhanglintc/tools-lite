# Validate Binary Search Tree
# for leetcode problems
# 2014.09.01 by zhanglin

# Problem:
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST_heper(self, root, lst):
        if root == None:
            return root

        self.isValidBST_heper(root.left, lst)
        lst.append(root.val)
        self.isValidBST_heper(root.right, lst)

    def isValidBST(self, root):
        lst = []
        self.isValidBST_heper(root, lst)

        if len(lst) == 0 or len(lst) == 1:
            return True

        for i in range(len(lst) - 1):
            if lst[i] >= lst[i + 1]:
                return False

        return True
