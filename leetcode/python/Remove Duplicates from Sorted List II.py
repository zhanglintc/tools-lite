# Remove Duplicates from Sorted List II
# for leetcode problems
# 2014.09.11 by zhanglin

# Problem:
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        new_head = ListNode(0)
        new_head.next = head
        pre = new_head
        cur = head

        while cur != None and cur.next != None: # while not the end
            jump_flag = False
            while cur.next != None and cur.val == cur.next.val: # while cur == cur.next, this can make cur travel to the last duplicate node
                cur = cur.next
                jump_flag = True

            cur = cur.next # no matter what,  move foreward

            if jump_flag: # if flag, jump over this cur
                pre.next = cur
            else: # if !flag, pre move foreward
                pre = pre.next

        return new_head.next

