# Remove Duplicates from Sorted List
# for leetcode problems
# 2014.09.11 by zhanglin

# Problem:
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        pointer = head

        while pointer != None and pointer.next != None:
            while pointer.next != None and pointer.val == pointer.next.val:
                pointer.next = pointer.next.next

            pointer = pointer.next

        return head

