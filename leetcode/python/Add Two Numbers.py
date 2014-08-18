# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None and l2 == None:
            return None

        new_head = ListNode(0)
        cache = new_head
        cur = new_head
        add_flag = 0

        # both list
        while l1 != None and l2 != None:
            cur.val = ((l1.val + l2.val + 1) if add_flag else (l1.val + l2.val))
            add_flag = 0

            if cur.val >= 10:
                cur.val %= 10
                add_flag = 1

            cur.next = ListNode(0)
            cache = cur
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        # l1 and !l2
        while l1 != None and l2 == None:
            cur.val = ((l1.val + 1) if add_flag else l1.val)
            add_flag = 0

            if cur.val >= 10:
                cur.val %= 10
                add_flag = 1

            cur.next = ListNode(0)
            cache = cur
            cur = cur.next
            l1 = l1.next

        # !l1 and l2
        while l1 == None and l2 != None:
            cur.val = ((l2.val + 1) if add_flag else l2.val)
            add_flag = 0

            if cur.val >= 10:
                cur.val %= 10
                add_flag = 1

            cur.next = ListNode(0)
            cache = cur
            cur = cur.next
            l2 = l2.next

        # set the tail
        if add_flag == 1:
            cache.next = ListNode(1)
        else:
            cache.next = None

        return new_head

