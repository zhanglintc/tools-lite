# Merge Two Sorted Lists
# for leetcode problems
# 2014.09.27 by zhanglin

# Problem:
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr  = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next

            else: # l1.val >= l2.val
                curr.next = l2
                l2 = l2.next
                curr = curr.next

        if l1:
            curr.next = l1

        else: # l2
            curr.next = l2

        return dummy.next


