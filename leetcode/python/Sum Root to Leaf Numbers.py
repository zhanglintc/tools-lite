# Sum Root to Leaf Numbers
# for leetcode problems
# 2014.09.14 by zhanglin

# Problem:
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# For example,

#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.

# Return the sum = 12 + 13 = 25.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.sumNumbers_helper(root, 0)

    def sumNumbers_helper(self, root, val):
        if root == None:
            return 0

        val = val * 10 + root.val

        if root.left == None and root.right == None:
            return val

        return self.sumNumbers_helper(root.left, val) + self.sumNumbers_helper(root.right, val)



