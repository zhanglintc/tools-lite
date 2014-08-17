# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        lst = []
        self.helper(root, lst)
        return lst        

    def helper(self, root, lst):
        if root != None and root != []:
            lst.append(root.val)
            self.helper(root.left,  lst)
            self.helper(root.right, lst)
