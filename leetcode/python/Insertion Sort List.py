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
        pt_head  = None

        while head != None and head.next != None: # until the end of head list
            if new_head.next == None: # the new_head is NULL
                new_head.next = head # copy the first node of head to new_head
                new_head.next.next = None #set the end of new_head as NULL
                #the line above is not correct, try to fix it in the next edition
            else: # the new_head is not NULL
                pt_cache = new_head
                pt_currt = new_head.next
                while pt_currt != None: # until the end
                    if head.val <= pt_currt.val:
                        pt_cache.next = head
                        pt_cache.next.next = pt_currt
                        break
                    else:
                        pt_cache = pt_cache.next
                        pt_currt = pt_currt.next
                        break

                    pt_cache.next = head
                    pt_cache.next.next = None

            head = head.next

        return new_head.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

lst = [10,223,88,1,3,11]

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


