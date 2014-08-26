# Convert Sorted Array to Binary Search Tree
# for leetcode problems
# 2014.08.26 by zhanglin

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST_helper(self, num, root):
        if num == []:
            return None

        mid = len(num) // 2
        root.val   = num[mid]
        root.left  = TreeNode(0)
        root.right = TreeNode(0)

        root.left  = self.sortedArrayToBST_helper(num[:mid], root.left)
        root.right = self.sortedArrayToBST_helper(num[mid + 1:], root.right)

        return root

    def sortedArrayToBST(self, num):
        root = TreeNode(0)
        root = self.sortedArrayToBST_helper(num, root)
        return root

