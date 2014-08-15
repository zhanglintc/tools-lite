# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None or head.next == None:
            return head

        new_head = ListNode(0)
        pt_cache = None
        pt_currt = None

        while head != None: # until the end of head list
            if new_head.next == None: # the new_head is NULL
                new_head.next = head # copy the first node of head to new_head
                head = head.next # move forward before set as NULL
                new_head.next.next = None #set the end of new_head as NULL
            else: # the new_head is not NULL
                pt_cache = new_head
                pt_currt = new_head.next
                while pt_currt != None: # until the end
                    if head.val <= pt_currt.val: # less than current, insert before current
                        pt_cache.next = head
                        head = head.next # move forward
                        pt_cache.next.next = pt_currt
                        break
                    else: # move forward
                        pt_cache = pt_cache.next
                        pt_currt = pt_currt.next
                        head = head.next # move forward before set as NULL
                        continue

                pt_cache.next = head
                if head != None:
                    pt_cache.next.next = None

        return new_head.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def debug_print(lst):
    while lst != None:
        print (lst.val)
        lst = lst.next

lst = [11111,1111,111,11,1]

head = ListNode(0)
pt = head # point to the head
for i in lst:
    node = ListNode(i) # new a node
    if head.next == None:
        head.next = node
    else:
        pt.next = node
    pt = pt.next

pt = head.next

S = Solution()

pt = S.insertionSortList(pt)

debug_print(pt)


