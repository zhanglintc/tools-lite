# Partition List
# for leetcode problems
# 2014.11.24 by zhanglin

# Problem:
# Given a linked list and a value x, 
# partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        dummy_smaller = ListNode(0)
        dummy_bigger  = ListNode(0)
        smaller = dummy_smaller
        bigger  = dummy_bigger

        while head:
            if head.val < x:
                smaller.next = head # append head to the end of smaller
                smaller = smaller.next # smaller point to next
                head = head.next # head point to next
                smaller.next = None # cut the end of smaller

            else: # head.val >= x
                bigger.next = head # append head to the end of bigger
                bigger = bigger.next # bigger point to next
                head = head.next # head point to next
                bigger.next = None # cut the end of bigger

        smaller.next = dummy_bigger.next # concatenate smaller and bigger

        return dummy_smaller.next # return the new linked_list




