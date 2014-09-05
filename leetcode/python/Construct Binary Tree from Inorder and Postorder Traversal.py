# Construct Binary Tree from Inorder and Postorder Traversal
# for leetcode problems
# 2014.09.05 by zhanglin

# Problem:
# Given inorder and postorder traversal of a tree, construct the binary tree.

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
    def buildTree(self, inorder, postorder):
        if inorder == [] or postorder == []:
            return None

        root = TreeNode(0)
        self.buildTree_helper(inorder, postorder, root)

        return root

    def buildTree_helper(self, inorder, postorder, root):
        if inorder == [] or postorder == []:
            return None

        cur = postorder[-1]         # see "Construct Binary Tree from Preorder and Inorder Traversal.py"
        idx = inorder.index(cur)
        root.val = cur

        root.left = TreeNode(0)
        root.right = TreeNode(0)

        root.left  = self.buildTree_helper(inorder[0 : idx],    postorder[0 : idx],  root.left)
        root.right = self.buildTree_helper(inorder[idx + 1 : ], postorder[idx : -1], root.right)

        return root

