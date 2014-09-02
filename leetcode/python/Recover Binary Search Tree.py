# Recover Binary Search Tree
# for leetcode problems
# 2014.09.02 by zhanglin

# Problem:
# Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.

# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree_helper(self, root, lst): # lst[0]: pre,  lst[1]: mistake1,  lst[2]: mistake2
        if root == None:
            return root

        self.recoverTree_helper(root.left, lst)

        if lst[0] == None:
            lst[0] = root

        else:
            if lst[0].val > root.val and lst[1] == None:
                lst[1] = lst[0]
                lst[2] = root

            elif lst[0].val > root.val and lst[1] != None:
                lst[2] = root

            lst[0] = root

        self.recoverTree_helper(root.right, lst)

    def recoverTree(self, root):
        lst = [None, None, None]
        self.recoverTree_helper(root, lst)
        lst[1].val, lst[2].val = lst[2].val, lst[1].val
        return root
