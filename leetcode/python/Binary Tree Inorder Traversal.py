# Binary Tree Inorder Traversal
# for leetcode problems
# 2014.08.29 by zhanglin

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        lst = []
        self.helper(root, lst)
        return lst        

    def helper(self, root, lst):
        if root != None and root != []:
            self.helper(root.left,  lst)
            lst.append(root.val)
            self.helper(root.right, lst)
