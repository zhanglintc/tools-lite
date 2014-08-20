# Reorder List
# for leetcode problems
# 2014.08.17 by zhanglin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None:
            return head
        stack = []
        current = head.next
        while current != None:
            stack.append(current)
            current = current.next

        current = head
        switch = 0
        while stack != []:
            if switch & 0x01:
                current.next = stack.pop(0)
            else:
                current.next = stack.pop()
            current = current.next
            switch += 1

        current.next = None

        return head

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

pt = S.reorderList(pt)

while pt != None:
    print (pt.val)
    pt = pt.next
