# Path Sum
# for leetcode problems
# 2014.08.24 by zhanglin

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum_helper(self, root, sum, pathsum):
        if root == None:
            return False

        if root.left == None and root.right == None:
            return (pathsum + root.val) == sum

        left  = self.hasPathSum_helper(root.left,  sum, pathsum + root.val)
        right = self.hasPathSum_helper(root.right, sum, pathsum + root.val)
        return left or right

    def hasPathSum(self, root, sum):
        return self.hasPathSum_helper(root, sum, 0)

