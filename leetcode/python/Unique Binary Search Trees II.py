# Unique Binary Search Trees II
# for leetcode problems
# 2014.08.31 by zhanglin

# Problem:
# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees_helper(self, start, end):
        lst = []

        if start > end:
            lst.append(None)
            return lst

        for i in range(start, end + 1):
            left  = self.generateTrees_helper(start, i - 1)
            right = self.generateTrees_helper(i + 1, end)

            for j in range(len(left)):
                for k in range(len(right)):
                    root = TreeNode(i)
                    root.left  = left[j]
                    root.right = right[k]
                    lst.append(root)

        return lst

    def generateTrees(self, n):
        return self.generateTrees_helper(1, n)
