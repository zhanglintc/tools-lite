# Balanced Binary Tree
# for leetcode problems
# 2014.08.21 by zhanglin

# Problem:
# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def helper(self, root):
        if not root:
            return 0

        return max(self.helper(root.left), self.helper(root.right)) + 1

    def isBalanced(self, root):
        # return True if self.helper(root) else False # set depth as anything except 0 is OK
        if not root:
            return True

        if abs(self.helper(root.left) - self.helper(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

        else:
            return False


