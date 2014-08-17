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
        cur = new_head
        add_flag = 0

        while l1 != None and l2 != None:
            cur.val = ((l1.val + l2.val + 1) if add_flag else (l1.val + l2.val))

            if cur.val >= 10:
                cur.val %= 10
                add_flag = 1
            
            l1 = l1.next
            l2 = l2.next

            if l1 == None and l2 != None:
                cur.next = l2
                break
            elif l2 == None and l1 != None:
                cur.next = l1
                break
            elif l1 == None and l2 == None and add_flag == 0:
                cur.next = None
                break

            cur.next = ListNode(0)
            cur = cur.next
            add_flag = 0  

        return new_head

