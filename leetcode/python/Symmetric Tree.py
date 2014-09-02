# Symmetric Tree
# for leetcode problems
# 2014.09.02 by zhanglin

# Problem:
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric_helper(self, left, right):
        if left == None and right == None:
            return True

        if (left == None and right != None) or (left != None and right == None) or (left.val != right.val):
            return False

        return self.isSymmetric_helper(left.left, right.right) and self.isSymmetric_helper(left.right, right.left)

    def isSymmetric(self, root):
        if root == None:
            return True

        return self.isSymmetric_helper(root.left, root.right)
