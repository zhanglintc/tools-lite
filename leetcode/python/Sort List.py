# Sort List
# for leetcode problems
# 2014.08.13 by zhanglin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None or head.next == None: # only one node
            return head

        new_head_1st = ListNode(0) # two new head
        new_head_2nd = ListNode(0)
        pointer = head.next # skip the first node

        cur_1st = new_head_1st
        cur_2nd = new_head_2nd

        while pointer != None: # until the end
            if pointer.val <= head.val:
                cur_1st.next = pointer
                cur_1st = cur_1st.next
            else:
                cur_2nd.next = pointer
                cur_2nd = cur_2nd.next
            pointer = pointer.next # point to the next one

        cur_1st.next = None # cut the end

        cur_2nd.next = head # add the first node to the end of cur_2nd
        head.next = None # cut the end

        cur_1st = new_head_1st.next
        cur_2nd = new_head_2nd.next

        cur_1st = self.sortList(cur_1st)
        cur_2nd = self.sortList(cur_2nd)

        pointer = cur_1st

        if pointer == None:
            return cur_2nd

        while pointer.next != None: # find the end
            pointer = pointer.next

        pointer.next = cur_2nd

        return cur_1st

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

# pt = head.next
# while pt != None:
#     print (pt.val)
#     pt = pt.next

def debug_print(lst):
    while lst != None:
        print (lst.val)
        lst = lst.next

pt = head.next

S = Solution()

pt = S.sortList(pt)

while pt != None:
    print (pt.val)
    pt = pt.next