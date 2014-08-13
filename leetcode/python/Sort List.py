# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def merge(self, lst1, lst2):
        if lst1 == None:
            return lst2
        if lst2 == None:
            return lst1

        new_lst = ListNode(0) # new a linded list
        pointer = new_lst

        while lst1 != None and lst2 != None:
            if lst1.val < lst2.val:
                pointer.next = lst1
                lst1 = lst1.next
            else:
                pointer.next = lst2
                lst2 = lst2.next
            pointer = pointer.next

        if lst1 == None:
            pointer.next = lst2
        if lst2 == None:
            pointer.next = lst1

        return new_lst.next

        
    def sortList(self, head):
        if head == None or head.next == None: # only one node
            return head

        fast = head
        slow = head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        new_head_1st = head
        new_head_2nd = slow.next
        slow.next = None #cut the linked list

        new_head_1st = self.sortList(new_head_1st)
        new_head_2nd = self.sortList(new_head_2nd)

        return self.merge(new_head_1st, new_head_2nd)

# This version is using Merge Sort, but failed bacause of LTE.
