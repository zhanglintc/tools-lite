# Insertion Sort List
# for leetcode problems
# 2014.08.15 by zhanglin

# Problem:
# Sort a linked list using insertion sort.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        current = head
        while current.next:
            if current.val < current.next.val: # if sorted, move forward
                current = current.next

            else: # this node need to be inserted to previous sorted list
                insertPos = dummy # find insertion position from the very beginning
                while insertPos.next.val < current.next.val: # find appropriate position
                    insertPos = insertPos.next

                # after while loop, now insertPos.val <= TobeMoved.val <= insertPos.next.val
                # then insert TobeMoved between insertPos and insertPos.next
                TobeMoved = current.next
                current.next = TobeMoved.next
                TobeMoved.next = insertPos.next
                insertPos.next = TobeMoved

        return dummy.next


