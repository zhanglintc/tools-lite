# Minimum Depth of Binary Tree
# for leetcode problems
# 2014.08.20 by zhanglin

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
            return root

        left  = self.helper(root.left,  counter)
        right = self.helper(root.right, counter)

        if left != None and right != None:
            return min(left, right) + 1
        elif left == None and right != None:
            return right + 1
        elif left != None and right == None:
            return left + 1
        else: # left is None and right is None
            return counter + 1

    def minDepth(self, root):
        min_depth = self.helper(root, 0)
        return (0 if min_depth == None else min_depth)

