# Convert Sorted List to Binary Search Tree
# for leetcode problems
# 2014.08.27 by zhanglin

# Definition for a  binary tree node
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
        if head == None: # here is the bug
            return None

        fast = head
        slow = head
        root.left  = TreeNode(0)
        root.right = TreeNode(0)

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        cache = slow
        slow = slow.next
        cache.next = None

        root.val   = cache.val

        root.left  = self.sortedListToBST_helper(head, root.left)
        root.right = self.sortedListToBST_helper(slow, root.right)

        return root

    def sortedListToBST(self, head):
        root = TreeNode(0)
        return self.sortedListToBST_helper(head, root)
