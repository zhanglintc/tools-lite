# Binary Tree Maximum Path Sum
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
    def maxPathSum_helper(self, root, lst):
        if root == None:
            return 0

        left  = self.maxPathSum_helper(root.left,  lst) # find max of left
        right = self.maxPathSum_helper(root.right, lst) # find max of right
        max_sum_add = max(root.val, left + root.val, right + root.val, left + root.val + right) # for append to lst
        max_sum_ret = max(root.val, left + root.val, right + root.val) # for return
        lst.append(max_sum_add) # add this node's max to lst
        return max_sum_ret # return max value through this node

    def maxPathSum(self, root):
        lst = []
        self.maxPathSum_helper(root, lst)
        if lst != []:
            return max(lst)
        # other: (means lst == [])
        #   return None
