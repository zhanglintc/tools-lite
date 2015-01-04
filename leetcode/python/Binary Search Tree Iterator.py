# Binary Search Tree Iterator
# for leetcode problems
# 2015.01.04 by zhanglin

# Problem:
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stk = []

        while root:
            self.stk.append(root)
            root = root.left

        self.this = root

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return not self.stk == []

    # @return an integer, the next smallest number
    def next(self):
        node = self.stk.pop()
        this = node.right

        while this:
            self.stk.append(this)
            this = this.left

        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


