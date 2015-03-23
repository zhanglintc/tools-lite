# Maximum Depth of Binary Tree
# for leetcode problems
# 2014.08.20 by zhanglin

# Problem:
# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def helper(self, root, counter):
        if root == None:
            return counter

        return max(self.helper(root.left, counter), self.helper(root.right, counter)) + 1

    def maxDepth(self, root):
        return self.helper(root, 0)


