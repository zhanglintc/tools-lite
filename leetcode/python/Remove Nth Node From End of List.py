# Remove Nth Node From End of List
# for leetcode problems
# 2014.09.22 by zhanglin

# Problem:
# Given a linked list, remove the n[th] node from the end of list and return its head.

# For example,

# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Note:
# Given n will always be valid.
# Try to do this in one pass.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for i in range(n): # make fast n steps ahead of slow
            fast = fast.next

        while fast.next: # while fast not reach the end
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next # remove slow.next

        return dummy.next #return


