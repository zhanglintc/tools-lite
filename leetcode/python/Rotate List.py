# Rotate List
# for leetcode problems
# 2015.01.07 by zhanglin

# Problem:
# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head:
            return head

        # make a dummy
        dummy = ListNode(0)
        dummy.next = head

        # count the length
        count = 0
        while head:
            count += 1
            head = head.next

        # calculate real k
        k %= count

        # if k == 0, return directly
        if not k:
            return dummy.next

        # tow pointers
        fast = dummy
        slow = dummy

        # make fast k steps ahead of slow
        for i in range(k):
            fast = fast.next

        # while not the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # rearrang only when slow is not the same to dummy
        if slow != dummy:
            fast.next = dummy.next
            dummy.next = slow.next
            slow.next = None

        return dummy.next


