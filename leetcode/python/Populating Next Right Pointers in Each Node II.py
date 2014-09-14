# Populating Next Right Pointers in Each Node II
# for leetcode problems
# 2014.09.14 by zhanglin

# Problem:
# Follow up for problem "Populating Next Right Pointers in Each Node".

# What if the given tree could be any binary tree? Would your previous solution still work?

# Note:
# You may only use constant extra space.

# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if (root == None) or (root.left == None and root.right == None): # node is None or node has no children
            return root

        if root.left != None: # root.left is not None
            if root.right != None: # root.right is not None, left to right
                root.left.next = root.right

            elif root.right == None: # if root.right is None
                explorer = root.next # find next
                while explorer != None:
                    if explorer.left != None:
                        root.left.next = explorer.left
                        break

                    if explorer.right != None:
                        root.left.next = explorer.right
                        break

                    explorer = explorer.next

        if root.right != None: # root.right is not None
            explorer = root.next
            while explorer != None:
                if explorer.left != None:
                    root.right.next = explorer.left
                    break

                if explorer.right != None:
                    root.right.next = explorer.right
                    break

                explorer = explorer.next

        self.connect(root.left)
        self.connect(root.right)


