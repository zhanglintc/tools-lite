# Linked List Cycle
# for leetcode problems
# 2014.09.10 by zhanglin

# Problem:
# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

