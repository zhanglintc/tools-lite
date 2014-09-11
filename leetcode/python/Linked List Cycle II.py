# Linked List Cycle II
# for leetcode problems
# 2014.09.10 by zhanglin

# Problem:
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        fast = head
        slow = head

        while fast != None and fast.next != None: # while not the end
            fast = fast.next.next
            slow = slow.next

            if fast == slow: # there is a circle
                fast = head # reset fast to head

                while fast != slow: # while not meet
                    fast = fast.next
                    slow = slow.next

                return fast # return the meet position

        return None # no circle return None

