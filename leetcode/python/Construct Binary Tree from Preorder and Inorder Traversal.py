# Construct Binary Tree from Preorder and Inorder Traversal
# for leetcode problems
# 2014.09.04 by zhanglin

# Problem:
# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if preorder == [] or inorder == []:
            return None

        root = TreeNode(0)
        self.buildTree_helper(preorder, inorder, root)

        return root

    def buildTree_helper(self, preorder, inorder, root):
        if preorder == [] or inorder == []:
            return None

        if len(preorder) == 1 or len(inorder) == 1:
            root.val = preorder[0]
            return None

        cur = preorder[0]
        idx = inorder.index(cur)
        root.val = cur

        root.left = TreeNode(0)
        root.right = TreeNode(0)

        self.buildTree_helper(preorder[1 : idx + 1], inorder[0 : idx], root.left)
        self.buildTree_helper(preorder[idx + 1 : ], inorder[idx + 1 : ], root.right)

