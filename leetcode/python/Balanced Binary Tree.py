# Balanced Binary Tree
# for leetcode problems
# 2014.08.21 by zhanglin

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced_helper(self, root, counter, result):
        if root == None or result[0] == False:
            return counter

        left  = self.isBalanced_helper(root.left,  counter, result)
        right = self.isBalanced_helper(root.right, counter, result)

        if abs(left - right) > 1:
            result[0] = False

        return max(left, right) + 1

    def isBalanced(self, root):
        result = [True]
        self.isBalanced_helper(root, 0, result)
        return result[0]
