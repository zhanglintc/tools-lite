# Convert Sorted List to Binary Search Tree
# for leetcode problems
# 2014.08.27 by zhanglin

# Problem:
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST_helper(self, head, root):
        root.left  = TreeNode(0)
        root.right = TreeNode(0)

        if head == None: # no node
            return None

        if head.next == None: # one node
            root.val   = head.val
            root.left  = None
            root.right = None
            return root

        if head.next.next == None: # two nodes
            root.val   = head.next.val
            head.next  = None
            root.left  = self.sortedListToBST_helper(head,  root.left)
            root.right = self.sortedListToBST_helper(None, root.right)
            return root

        fast = head
        slow = head
        prev = head

        while fast.next != None and fast.next.next != None: # three or more nodes
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        if fast.next == None: # odd
            left = head
            right = slow.next
            root.val = slow.val
            prev.next = None

        elif fast.next.next == None: # even
            left = head
            right = slow.next.next
            root.val = slow.next.val
            slow.next = None

        root.left  = self.sortedListToBST_helper(left,  root.left)
        root.right = self.sortedListToBST_helper(right, root.right)

        return root

    def sortedListToBST(self, head):
        root = TreeNode(0)
        return self.sortedListToBST_helper(head, root)


