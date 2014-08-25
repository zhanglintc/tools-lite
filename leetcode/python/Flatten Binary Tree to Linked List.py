# Flatten Binary Tree to Linked List
# for leetcode problems
# 2014.08.25 by zhanglin

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten_helper(self, root, pointer):
        if root == None:
            return root

        left  = root.left
        right = root.right

        pointer.right = root
        pointer.left = None
        pointer = pointer.right

        self.flatten_helper(left, pointer)
        self.flatten_helper(right, pointer)

    def flatten(self, root):
        pointer = TreeNode(0)
        self.flatten_helper(root, pointer)
        
