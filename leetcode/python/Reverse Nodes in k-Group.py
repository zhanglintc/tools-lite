# Reverse Nodes in k-Group
# for leetcode problems
# 2014.12.08 by zhanglin

# Problem:
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# You may not alter the values in the nodes, only nodes itself may be changed.
# Only constant memory is allowed.

# For example,
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # get linked list length
        p = head
        length = 0
        while p:
            length += 1
            p = p.next

        # set a dummy_head
        dummy_head = ListNode(0)
        dummy_head.next = head
        before_rev_end = dummy_head

        # reversing
        while length >= k:
            headPrev = before_rev_end
            headNext = head.next
            to_be_rev_head = before_rev_end.next

            idx = 1
            while idx < k:
                head.next = headPrev
                headPrev = head
                head = headNext
                headNext = headNext.next
                idx += 1

            head.next = headPrev
            to_be_rev_head.next = headNext
            before_rev_end.next = head

            # reset
            before_rev_end = to_be_rev_head
            head = to_be_rev_head.next

            length -= k

        return dummy_head.next


