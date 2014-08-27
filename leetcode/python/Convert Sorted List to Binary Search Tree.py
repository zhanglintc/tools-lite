# Convert Sorted List to Binary Search Tree
# for leetcode problems
# 2014.08.27 by zhanglin

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST_helper(self, head, root):
        if head == None:
            return None

        if head.next == None:
            root.val = head.val
            return root

        fast = head
        slow = head
        prev = head
        root.left  = TreeNode(0)
        root.right = TreeNode(0)

        while fast.next != None and fast.next.next != None:
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
            prev.next = None

        root.left  = self.sortedListToBST_helper(left,  root.left)
        root.right = self.sortedListToBST_helper(right, root.right)

        return root

    def sortedListToBST(self, head):
        root = TreeNode(0)
        return self.sortedListToBST_helper(head, root)
'''
Input:  {1,3}
Output: {1,1,3}
Expected:   {3,1}
'''

head = ListNode(1)
head.next = ListNode(2)

s = Solution()
s.sortedListToBST(head)